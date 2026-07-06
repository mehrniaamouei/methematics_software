import numpy as np
from scipy.integrate import simpson, trapezoid, quad

def f(x):
    return np.exp(x**2)

x = np.linspace(0, 1, 1001)
y = f(x)

simpson_result = simpson(y, x=x)

trapezoid_result = trapezoid(y, x=x)

quad_result, error = quad(f, 0, 1)

print("Simpson =", simpson_result)
print("Trapezoid =", trapezoid_result)
print("Gaussian (quad) =", quad_result)
print("Estimated Error =", error)