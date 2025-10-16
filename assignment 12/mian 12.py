#pralhad GOverdhan Gadagi
#2311130
from mylibrary import *

def f(x):
    return x**2/(1+x**4)
val=guassquadrature(14,f,-1,1)
print("value of integral",val)
print("=========================")
#question 2
def g(x):
    return np.sqrt(1+x**4)
valsimp=simpson(0,1,g,24)
valguass=guassquadrature(8,g,0,1)
print("value of integral using simpson ",valsimp)
print("value of integral using guass quadrature",valguass)