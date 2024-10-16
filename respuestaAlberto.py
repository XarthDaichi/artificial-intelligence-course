from sympy import symbols, diff, solve

x = symbols('x')

def f(x):
    return 2/3 * x ** 3 - 7/4 * x ** 2 + 3/2 * x + 1

derivada = diff(f(x), x)

puntos_criticos = solve(derivada, x)

segunda_derivada