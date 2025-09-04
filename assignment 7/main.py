#Pralhad Goveredhan Gadagi
#2311130
import math
def function(x):
    return 3*x + math.sin(x) - math.exp(x)

def df(x):
    return 3 + math.cos(x) - math.exp(x)

counter = 0

def bisection(a,b,accu,f):
    global counter
    counter = counter + 1
    if abs(a-b) < accu and (f(a) < accu or f(b) < accu) :
        return a
    else:
        c=(a+b)/2
        if f(c)*f(a) < 0 :

            a,b = a,c
        if f(c)*f(b) < 0 :
            a,b = c,b
        return bisection(a,b,accu,f)

counter1=0
def regula_falsi(a,b,accu,f,cprev=None):
    global counter1
    counter1= counter1+1
    c = b - ((b - a) * f(b)) / (f(b) - f(a))
    if cprev is not None and abs(cprev-c) < accu :
        return c

    if f(a)*f(c) < 0:
        a,b=a,c
    if f(b)*f(c) < 0:
        a,b=c,b

    return regula_falsi(a,b,accu ,f,c)
def newton_raphson(f,df,accu,x,itrations ):
    global i
    for i in range (itrations):
        x1=x - f(x)/df(x)
        if abs(x1-x) < accu:
            print("root at: ")
            return x1
        x=x1

root1=bisection(-1.5,1.5,10e-6,function)
print("using bisection \n ", root1,"in ith convergence", counter)
root2=regula_falsi(-1.5,1.5,10e-6,function)
print("using regula falsi \n", root2,"in ith convergence",counter1)
root=newton_raphson(function,df,10e-6,0,100)
print("using newton raphson\n",root,"in ith convergence", i)

#Question 2
print("==================================")
def funct(x):
    return (x**2 - 2*x -3)
def gunct(x):
    return math.sqrt(2*x + 3)

def fixedpt(x,g,accu,itration):
    for i in range (itration):
        x1=g(x)

        if abs(x1-x) < accu :
            print("i ith itration\n" , i)
            return x
        x=x1
ro=fixedpt(1,gunct,10e-6,100)
print("fixed pt method \n",ro)

'''
using bisection 
  0.36042022705078125 in ith convergence 20
using regula falsi 
 0.36042224320129207 in ith convergence 10
root at: 
using newton raphson
 0.3604217029603242 in ith convergence 3
==================================
i ith itration
 12
fixed pt method 
 2.999991937956321

'''