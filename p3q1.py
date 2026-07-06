import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sympy as sp
from fractions import Fraction

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 3, 5, 8, 5, 2])

X = sp.Symbol('X')
n = len(x)
L = 0
for i in range(n):
    li = 1
    for j in range(n):
        if j != i:
            li *= (X - x[j]) / (x[i] - x[j])
    L += y[i] * li

L_func = sp.expand(L)

print("="*80)
print("LAGRANGE INTERPOLATION POLYNOMIAL:")
print("="*80)

print("Decimal form:")
print("P(x) =", sp.N(L_func))
print()



cs = CubicSpline(x, y, bc_type='natural')

print("="*80)
print("NATURAL CUBIC SPLINE INTERPOLATION:")
print("="*80)
for i in range(len(x)-1):
    coefs = cs.c[:, i]
    print(f"Interval [{x[i]:.0f}, {x[i+1]:.0f}]:")
    print(f"  S(x) = {coefs[0]:.6f}*(x-{x[i]:.0f})^3 + {coefs[1]:.6f}*(x-{x[i]:.0f})^2 + {coefs[2]:.6f}*(x-{x[i]:.0f}) + {coefs[3]:.6f}")
    print()

L_lambdified = sp.lambdify(X, L_func, 'numpy')
x_plot = np.linspace(1, 6, 100)
y_Lagrange = L_lambdified(x_plot)
y_Spline = cs(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', markersize=10, label='Data Points')
plt.plot(x_plot, y_Lagrange, 'b-', linewidth=2, label='Lagrange')
plt.plot(x_plot, y_Spline, 'g--', linewidth=2, label='Natural Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Lagrange and Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()