# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:10:32 2025

@author: Mohammad
"""

# Finite Element Method for 1D Boundary Value Problem
# Complete working implementation

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la


# 1. Define the exact solution and right-hand side
def exact_solution(x):
    """Exact solution to the boundary value problem."""
    return x * (1 - x) * np.exp(x)

def rhs_function(x):
    """Right-hand side function f(x) = -u''(x)."""
    return x * (x + 3) * np.exp(x)

# 2. Set up the finite element mesh
a = 0.0
b = 1.0
n_elements = 2
n_nodes = n_elements + 1
nodes = np.linspace(a, b, n_nodes)

# 3. Define basis functions
def linear_basis_function(i, x, nodes):
    """Evaluate the linear basis function φᵢ(x) at given points."""
    n = len(nodes) - 1
    
    if i == 0:
        result = np.where((nodes[0] <= x) & (x <= nodes[1]), 
                         (nodes[1] - x) / (nodes[1] - nodes[0]), 0)
    elif i == n:
        result = np.where((nodes[n-1] <= x) & (x <= nodes[n]),
                         (x - nodes[n-1]) / (nodes[n] - nodes[n-1]), 0)
    else:
        left_part = np.where((nodes[i-1] <= x) & (x <= nodes[i]),
                           (x - nodes[i-1]) / (nodes[i] - nodes[i-1]), 0)
        right_part = np.where((nodes[i] <= x) & (x <= nodes[i+1]),
                            (nodes[i+1] - x) / (nodes[i+1] - nodes[i]), 0)
        result = left_part + right_part
    
    return result

# 4. Set up numerical integration (Gaussian quadrature)
gauss_points = np.array([
    0.112701665379258311482073460022,
    0.5, 
    0.887298334620741688517926539978
])

gauss_weights = np.array([
    5.0 / 18.0,
    8.0 / 18.0, 
    5.0 / 18.0
])

# 5. Assemble the finite element system
def assemble_system(nodes, gauss_points, gauss_weights):
    """Assemble the finite element system A * u = F."""
    n_nodes = len(nodes)
    A = np.zeros((n_nodes, n_nodes))
    F = np.zeros(n_nodes)
    
    for e in range(len(nodes) - 1):
        x_left = nodes[e]
        x_right = nodes[e+1]
        element_length = x_right - x_left
        
        for q in range(len(gauss_points)):
            x_q = x_left + gauss_points[q] * element_length
            weight_q = gauss_weights[q] * element_length
            
            for i_local in range(2):
                i_global = e + i_local
                
                if i_local == 0:
                    phi_i_prime = -1.0 / element_length
                else:
                    phi_i_prime = 1.0 / element_length
                
                # Simplified basis function evaluation for load vector
                if i_local == 0:
                    phi_i = (x_right - x_q) / element_length
                else:
                    phi_i = (x_q - x_left) / element_length
                
                F[i_global] += weight_q * rhs_function(x_q) * phi_i
                
                for j_local in range(2):
                    j_global = e + j_local
                    
                    if j_local == 0:
                        phi_j_prime = -1.0 / element_length
                    else:
                        phi_j_prime = 1.0 / element_length
                    
                    A[i_global, j_global] += weight_q * phi_i_prime * phi_j_prime
    
    return A, F

# 6. Apply boundary conditions
def apply_boundary_conditions(A, F, nodes):
    """Apply Dirichlet boundary conditions u(0) = 0 and u(1) = 0."""
    A_mod = A.copy()
    F_mod = F.copy()
    
    n = len(nodes) - 1
    
    # Left boundary
    A_mod[0, :] = 0.0
    A_mod[0, 0] = 1.0
    F_mod[0] = exact_solution(nodes[0])
    
    # Right boundary  
    A_mod[n, :] = 0.0
    A_mod[n, n] = 1.0
    F_mod[n] = exact_solution(nodes[n])
    
    return A_mod, F_mod

# Main solution process
print("FEM1D - 1D Finite Element Method")
print("=" * 50)

# Assemble and solve
A, F = assemble_system(nodes, gauss_points, gauss_weights)
A_bc, F_bc = apply_boundary_conditions(A, F, nodes)
u_fem = la.solve(A_bc, F_bc)

# Compare with exact solution
u_exact_nodes = exact_solution(nodes)
errors = np.abs(u_exact_nodes - u_fem)

print("\nSolution Comparison:")
print("Node    x        u_FEM       u_exact     Error")
print("-" * 50)
for i in range(len(nodes)):
    print(f"{i:3d}  {nodes[i]:6.3f}  {u_fem[i]:10.6f}  {u_exact_nodes[i]:10.6f}  {errors[i]:10.2e}")

# Visualization
x_fine = np.linspace(a, b, 200)
u_exact_fine = exact_solution(x_fine)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_fine, u_exact_fine, 'r-', linewidth=2, label='Exact Solution')
plt.plot(nodes, u_fem, 'bo-', linewidth=2, markersize=6, label='FEM Solution')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Finite Element Solution')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(nodes, errors, 'ro-', linewidth=2, markersize=6)
plt.xlabel('x')
plt.ylabel('|Error|')
plt.title('Pointwise Error')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"\nMaximum Error: {np.max(errors):.2e}")
print(f"L2 Error Norm: {np.sqrt(np.mean(errors**2)):.2e}")