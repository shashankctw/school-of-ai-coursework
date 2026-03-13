import sympy as sp

# Define a multivariable function
x, y = sp.symbols('x y')
f = x**2 + 3*y**2 - 4*x*y + 5

# Compute partial derivatives
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("gradient with respect to x: ", grad_x)
print("gradient with respect to y: ", grad_y)