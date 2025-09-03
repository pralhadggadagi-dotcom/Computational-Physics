# Pralhad GOverdhan Gadagi
#2311130
import math
from mylibrary import *

#QUestion 1
def func(x):
    return math.log(x/2) - math.sin(5*x/2)

def bisection(a,b,accu,f):
    if abs(a-b) < accu and (f(a) < accu or f(b) < accu) :
        return a
    else:
        c=(a+b)/2
        if f(c)*f(a) < 0 :

            a,b = a,c
        if f(c)*f(b) < 0 :
            a,b = c,b
        return bisection(a,b,accu,f)
root1= bisection(1.5,3,10e-6 ,func)
def regula_falsi(a,b,accu,f,cprev=None):
    c = b - ((b - a) * f(b)) / (f(b) - f(a))
    if cprev is not None and abs(cprev-c) < accu :
        return c

    if f(a)*f(c) < 0:
        a,b=a,c
    if f(b)*f(c) < 0:
        a,b=c,b

    return regula_falsi(a,b,accu ,func,c)
root= regula_falsi(1.5,3,10e-6 ,func)

print("by bisection : \n",root1)
print("by regula falsi : \n",root)

#question 2
print("============================================")
print("quesiton 2")
def function(x):
    return -x - math.cos(x)
def bracketing(a,b,f):
    if f(a)*f(b) < 0 :
        return a,b
    if abs(f(a)) < abs(f(b)) :
        a= a - 0.1*(b-a)
    else:
        b=b + 0.1*(b-a)
    return bracketing(a,b,f)
lolimt,uplimit=bracketing(2,4,function)

print("interval is [ ",lolimt ,",", uplimit,"]")
ro=bisection(lolimt,uplimit,10e-6,function)
print("root is ", ro)
'''
by bisection : 
 2.623140335083008
by regula falsi : 
 2.6231403358555436
============================================
quesiton 2
interval is [  -1.1874849202000002 , 4 ]
root is  -0.7390931171954997
'''