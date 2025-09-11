from mylibrary import *
import math

def evalfun(coef, x):
    n = len(coef)
    result = 0
    for am in range(n):
        result = result + coef[am] * (x ** (n - am - 1))
    return result

def derivative(coef, x):
    n = len(coef)
    result = 0
    for am in range(n - 1):
        pow = n - am - 1
        result = result + pow * coef[am] * (x ** (pow - 1))
    return result

def doublederivative(coef, x):
    n = len(coef)
    result = 0
    for am in range(n - 2):
        pow = n - am - 1
        result = result + pow * (pow - 1) * coef[am] * (x ** (pow - 2))
    return result

def laguerre(coeff, x0, accu, intrations):
    n = len(coeff) - 1
    x = x0
    for some in range(intrations):
        p = evalfun(coeff, x)
        if abs(p) < accu:
            return x
        G = derivative(coeff, x) / p
        H = G ** 2 - doublederivative(coeff, x) / p
        shrus = math.sqrt(abs((n - 1) * (n * H - G ** 2)))
        denom1 = G + shrus
        denom2 = G - shrus
        denom = denom1
        if abs(denom1) < abs(denom2):
            denom = denom2
        a = n / denom
        x1 = x - a
        if abs(x1 - x) < accu:
            return x1
        x = x1
    return x

def deflation(coef, root):
    n = len(coef)
    newcoef = [coef[0]]
    for i in range(1, n):
        newcoef.append(coef[i] + root * newcoef[-1])
    return newcoef[:-1]

def laguerrefull(coeff, x):
    roots = []
    currcoeff = coeff[:]
    while len(currcoeff) > 1:
        root = laguerre(currcoeff, x, 1e-6, 100)
        roots.append(root)
        currcoeff = deflation(currcoeff, root)
    return roots

coeffs1 = [1, -1, -7, 1, 6]
print("Roots of P1:")
print(laguerrefull(coeffs1, 0))

coeffs2 = [1, 0, -5, 0, 4]
print("Roots of P2:")
print(laguerrefull(coeffs2, 1))

coeffs3 = [2, 0, -19.5, 0.5, 13.5, -4.5]
print("Roots of P3:")
print(laguerrefull(coeffs3, 2))

"""
Roots of P1:
[-1.0, 0.9999999999929003, -1.99999999999716, 3.0000000000042597]
Roots of P2:
[1, 1.9999999997991764, -0.9999999991967057, -2.000000000602471]
Roots of P3:
[0.5001154734922187, 0.4998845191418521, 2.999999998759261, -0.9999999900548966, -3.000000001338435]
"""
"""will add in lib later"""