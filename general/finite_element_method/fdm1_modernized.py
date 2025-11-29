#!/usr/bin/env python3
"""
FEM1D: Linear finite elements for -u'' = f on (0,1) with u(0)=u(1)=0.

Exact solution:
    u(x) = x(1-x)exp(x)
Right-hand side:
    f(x) = x(x+3)exp(x) = -u''(x)

Reference:
    Adapted and modernized from John Burkardt's FEM1D code
    (http://people.sc.fsu.edu/~jburkardt/py_src/fem1d/fem1d.py)

This script demonstrates:
    - Mesh generation
    - Element stiffness and load assembly
    - Dirichlet boundary condition enforcement
    - Solution of the linear system
    - Error norms and plotting
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
import time
from scipy.integrate import trapezoid


# --- Problem definition -------------------------------------------------------

def exact_fn(x):
    """Exact solution u(x) = x(1-x)exp(x)."""
    x = np.asarray(x)
    return x * (1.0 - x) * np.exp(x)

def rhs_fn(x):
    """Right-hand side f(x) = x(x+3)exp(x)."""
    x = np.asarray(x)
    return x * (x + 3.0) * np.exp(x)


# --- Quadrature ---------------------------------------------------------------

def gauss_legendre(nq=3):
    """Return nq-point Gauss–Legendre quadrature nodes/weights on [0,1]."""
    xg, wg = np.polynomial.legendre.leggauss(nq)  # [-1,1]
    xq = 0.5 * (xg + 1.0)
    wq = 0.5 * wg
    return xq, wq


# --- Dirichlet BC helper ------------------------------------------------------

def apply_dirichlet_bc(A, rhs, nodes, values):
    """
    Apply Dirichlet BCs symmetrically:
    zero row+col, set diagonal=1, rhs=value.
    """
    A = A.tolil()
    for k, v in zip(nodes, values):
        A[:, k] = 0.0
        A[k, :] = 0.0
        A[k, k] = 1.0
        rhs[k] = v
    return A.tocsr()


# --- Assembly -----------------------------------------------------------------

def assemble_system(n=20, nq=3):
    """
    Assemble global stiffness matrix A and load vector rhs
    for n linear elements on [0,1].
    """
    x = np.linspace(0.0, 1.0, n + 1)
    A = sp.lil_matrix((n + 1, n + 1), dtype=float)
    rhs = np.zeros(n + 1)

    xq_ref, wq_ref = gauss_legendre(nq)

    for e in range(n):
        xl, xr = x[e], x[e + 1]
        h = xr - xl
        # Local stiffness for linear element
        Ke = (1.0 / h) * np.array([[1.0, -1.0], [-1.0, 1.0]])
        # Quadrature points mapped to element
        xq = xl + h * xq_ref
        wq = h * wq_ref
        phi0 = (xr - xq) / h
        phi1 = (xq - xl) / h
        fe = np.array([np.sum(wq * phi0 * rhs_fn(xq)),
                       np.sum(wq * phi1 * rhs_fn(xq))])
        idx = np.array([e, e + 1])
        A[np.ix_(idx, idx)] += Ke
        rhs[idx] += fe

    # Dirichlet BCs at both ends
    u0 = float(exact_fn(x[0]))
    u1 = float(exact_fn(x[-1]))
    A = apply_dirichlet_bc(A, rhs, nodes=[0, n], values=[u0, u1])

    return A.tocsr(), rhs, x


# --- Solver -------------------------------------------------------------------

def solve_fem1d(n=20, nq=3, show_matrix=False):
    """Assemble and solve FEM system."""
    A, rhs, x = assemble_system(n, nq)

    if show_matrix:
        print("\nMatrix A and RHS vector:")
        for i in range(n + 1):
            row = " ".join(f"{A[i,j]:10.6f}" for j in range(n + 1))
            print(f"{row} | {rhs[i]:10.6f}")

    u = spla.spsolve(A.tocsc(), rhs)
    return x, u, rhs


# --- Error analysis -----------------------------------------------------------

def compute_errors(x, u):
    """Compute exact solution and error norms."""
    uex = exact_fn(x)
    err = u - uex
    linf = np.max(np.abs(err))
    l2 = np.sqrt(trapezoid(err**2, x))
    return uex, err, linf, l2


# --- Plotting -----------------------------------------------------------------

def plot_solution(x, u):
    """Plot FEM solution vs exact solution."""
    xp = np.linspace(0.0, 1.0, 401)
    up = exact_fn(xp)
    plt.figure(figsize=(7,4.2))
    plt.plot(x, u, "bo-", label="FEM (linear)")
    plt.plot(xp, up, "r", lw=2, label="Exact")
    plt.title("1D FEM: -u'' = f on (0,1)")
    plt.xlabel("x"); plt.ylabel("u(x)")
    plt.grid(alpha=0.3); plt.legend()
    plt.show()


# --- Main ---------------------------------------------------------------------

def fem1d_demo(n=20, nq=3, show_matrix=False):
    """
    Run FEM1D demo:
    - Assemble system
    - Solve
    - Print nodes, solution, errors
    - Plot results
    - Report timing
    """
    print("\nFEM1D")
    print("  Solving -u'' = x(x+3)exp(x), 0<x<1 with u(0)=u(1)=0")
    print(f"  Using {n} elements and {nq}-point Gauss–Legendre quadrature")

    t_wall_start = time.perf_counter()
    t_cpu_start = time.process_time()

    x, u, rhs = solve_fem1d(n, nq, show_matrix=show_matrix)
    uex, err, linf, l2 = compute_errors(x, u)

    print("\nNodes:")
    for i, xi in enumerate(x):
        print(f"  {i:3d} {xi:10.6f}")

    print("\nComputed solution vs exact at nodes:")
    print(f"{'Node':>4} {'Ucomp':>14} {'Uexact':>14} {'Error':>14}")
    for i in range(len(x)):
        print(f"{i:4d} {u[i]:14.6e} {uex[i]:14.6e} {err[i]:14.6e}")

    print(f"\nError norms: L_inf={linf:.6e}, L2={l2:.6e}")

    t_wall_end = time.perf_counter()
    t_cpu_end = time.process_time()
    print("\nTiming:")
    print(f"  Wall-clock time: {t_wall_end - t_wall_start:.6f} sec")
    print(f"  CPU process time: {t_cpu_end - t_cpu_start:.6f} sec")

    plot_solution(x, u)


if __name__ == "__main__":
    fem1d_demo(n=5, nq=3, show_matrix=True)
