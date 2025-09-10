#Pralhad Goverdhan Gadagi
#2311130

import math
from mylibrary import *

def function(x):
    ele1=x[0]**2 + x[1] -37
    ele2=x[0] - x[1]**2 -5
    ele3=x[0] + x[1] + x[2] -3
    lst1=[ele1,ele2,ele3]
    return lst1

def gunction(x):
    ele1=math.sqrt(37-x[1])
    ele2=math.sqrt(x[0]-5)
    ele3=3 -x[0] -x[1]
    lst1=[ele1,ele2,ele3]
    return lst1

def multifixedpt(x,g,accu,itration):
    for ig in range (itration):
        x1=g(x)
        sum = 0
        prosum = 0
        for i in range(len(x1)):
            ele = abs(x1[i] - x[i])
            sum = sum + ele
            prosum = prosum + x1[i] ** 2
        criteria = sum / math.sqrt(prosum)

        if criteria < accu :

            print("i ith itration\n" , ig)
            return x
        x=x1
guessx=[10,2,10]
print("using fixed point method")
solutions=multifixedpt(guessx,gunction,10e-10,1000)
print(solutions)
print("==============================================")
#part 2

def jacobian(x):
    ele1=[2*x[0],1,0]
    ele2=[1,-2*x[1],0]
    ele3=[1,1,1]
    return [ele1,ele2,ele3]
def multinewton_raphson(f,accu,x,itrations ):
    global indi
    for indi in range (itrations):
        jacobinv=gaussjordan_inverse(jacobian(x))
        fx=f(x)
        matmult=[]
        for an in range(len(jacobinv)):
            sum=0
            for nd in range(len(jacobinv[0])):
                sum=sum + jacobinv[an][nd] *f(x)[nd]
            matmult.append(sum)
        x1=[]
        for some in range(len(x)):
            imi=x[some]- matmult[some]
            x1.append(imi)
        sum = 0
        prosum = 0
        for i in range(len(x1)):
            ele = abs(x1[i] - x[i])
            sum = sum + ele
            prosum = prosum + x1[i] ** 2
        criteria = sum / math.sqrt(prosum)

        if criteria < accu :

            print("i ith itration\n" , indi)
            return x
        x=x1
guessx=[10,2,10]

sol=multinewton_raphson(function,10e-6,guessx,100)
print("using multivariable newton raphson\n",sol)

'''
using fixed point method
i ith itration
 15
[6.000000000018677, 0.9999999997210853, -3.999999999218048]
==============================================
i ith itration
 4
using multivariable newton raphson
 [5.999999635336607, 1.0000043921145025, -4.0000040274511095]
'''