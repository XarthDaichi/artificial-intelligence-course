import math

def f_derivate(f, x, epsilon=1e-3):
    return (f(x + epsilon) - f(x)) / epsilon 

def f_derivate_2(f, x, epsilon=1e-6):
    return (f(x + epsilon) - f(x - epsilon)) / 2 * epsilon

def f1(x):
    return x**2 - 2*x + 1

def f1_prime(x):
    return 2*x - 2

########################### SOME TEST CASES #######################

print("\n*** Testing f_derivate ***\n")
x = 5
print("Test Case 1: f(x) = x**2 -2x + 1, x = 5, epsilon=10^-6", ":", f1_prime(x), f_derivate(f1, x, 1e-10))
print()

def f2(x):
    return (math.sin(x))**2

def f2_prime(x):
    return math.sin(2*x)

x = 5
print("Test Case 2: f(x) = sin(x)^2, x = 5, epsilon=10^-6", ":", f2_prime(x), f_derivate(f2, x, 1e-10))
print()

def f3(x):
    return math.sin(x) * math.log10(3*x)

def f3_prime(x):
    return math.cos(x) * math.log10(3*x) + math.sin(x) * 3/(3*x * math.log(10))

print("Test Case 3: f(x) = log(3x^sin(x)), x = 5, epsilon=10^-6", ":", f3_prime(x), f_derivate(f3, x, 1e-10))
print()