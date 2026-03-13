import sympy as sp

# Define a function
x = sp.symbols('x')
f = x**3 - 5*x + 7

# Compute Derivative
derivative = sp.diff(f, x)

print("Function: ", f)
print("Derivative: ", derivative)