"""
Numerical Integration Module

Implements three quadrature rules:
- Trapezoidal rule
- Midpoint rule
- Simpson's rule

All functions accept:
  f : callable integrand
  a, b : integration limits (finite)
  n : number of subintervals (n >= 1)

Note: Simpson's rule requires n to be even (i.e., odd number of points).
Since we use n = 2^k + 1 (odd number of points), subinterval count = n-1 (even) — valid.
Thus, in this context, `n` = number of points.
"""

def trapezoidal(f, a, b, n):
    """
    Trapezoidal rule with n points (n-1 subintervals).
    """
    if n < 2:
        raise ValueError("n must be at least 2 (>=2 points)")
    h = (b - a) / (n - 1)
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n - 1):
        s += f(a + i * h)
    return h * s


def midpoint(f, a, b, n):
    """
    Midpoint rule using n subintervals (n function evaluations).
    Note: Here `n` = number of subintervals = number of points.
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    h = (b - a) / n
    s = 0.0
    for i in range(n):
        s += f(a + (i + 0.5) * h)
    return h * s


def simpson(f, a, b, n):
    """
    Simpson's rule using n points (n must be odd, n >= 3).
    
    Formula:
      ∫_a^b f(x) dx ≈ (h/3) [f(x0) + 4f(x1) + 2f(x2) + ... + 4f(x_{n-2}) + f(x_{n-1})]
      where h = (b - a)/(n - 1)
    
    Parameters:
      f : callable
      a, b : float — integration limits
      n : int — number of points (must be odd and >=3)
    
    Returns:
      float : integral approximation
    """
    if n < 3 or n % 2 == 0:
        raise ValueError("Simpson's rule requires n >= 3 and odd (n points)")
    h = (b - a) / (n - 1)
    s = f(a) + f(b)
    # Odd indices: coefficient 4
    for i in range(1, n - 1, 2):
        s += 4 * f(a + i * h)
    # Even indices: coefficient 2
    for i in range(2, n - 1, 2):
        s += 2 * f(a + i * h)
    return (h / 3.0) * s