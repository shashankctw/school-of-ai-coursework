import sympy as sp

# Define a function
x = sp.symbols('x')
f = sp.exp(-x)

# Compute indefinite integral
indefinite_integral = sp.integrate(f, x)
print("Indefinite Integral of exp(-x):", indefinite_integral)

# Compute definite integral
definite_integral = sp.integrate(f, (x, 0, sp.oo))
print("Definite Integral:", definite_integral)