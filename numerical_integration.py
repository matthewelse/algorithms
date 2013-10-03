import math

def func(x):
    # integral = (x**3)/3 + x^2
    return float(math.sin(x))

def integrate_trapezoidal(f, a, b, n=320000):
    # Calculate sum part of the formula...
    h = (b-a)/n
    _sum = 0
    for k in xrange(1, n):
        _sum += f(a + k*((b-a)/n))

    _sum += f(a)/2 + f(b)/2
    _sum *= (b-a)/n
    return _sum
    
print integrate_trapezoidal(func, 1.0, 2.0)
