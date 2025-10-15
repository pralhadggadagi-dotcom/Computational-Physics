#Pralhad Goverdhan Gadagi
#2311130
#question 1

from mylibrary import LCGrandom
import numpy as np
from mylibrary import *
import matplotlib.pyplot as plt

start = LCGrandom()
ni = 0
for i in range(50000):
    x_rand = start.generate()
    y_rand = start.generate()

    x = -2 + x_rand * (4)
    y = -1 + y_rand * (2)

    if (x**2 / 4 + y**2 / 1) <= 1:
        ni += 1
area = 8 * (ni / 50000)
print("Estimated area of ellipse ",area)
print("=====================================")
#question 2
import numpy as np

def f(x):
    return (x - 5) * np.exp(x) + 5

def df(x):
    return (x - 4) * np.exp(x)
xguess = 5
x = newton_raphson(f, df, 1e-4, xguess, 100)
print("x =", x)
h = 6.626*10e-34
k = 1.381*10e-23
c = 3.0*10e8
b = (h * c) / (k * x)

print("Wien's constant b = ",b," m·K")
print("=======================================")
#question 3
A = readmatrix("matrix")
n = len(A)
L, U = lu_decom(A)
I = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    I.append(row)
A_inv_cols = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(I[j][i])
    x = lu_solve(L, U, b)
    A_inv_cols.append(x)
A_inv = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(A_inv_cols[j][i])
    A_inv.append(row)

for i in range(n):
    for j in range(n):
        A_inv[i][j] = round(A_inv[i][j], 3)

print("Inverse of A:",A_inv)
print("=====================================")
#question 4
matA=readmatrix("matA")
vecB=readmatrix("vector B")
solut=guass_seidel(matA,vecB)
print(solut)

'''
Estimated area of ellipse  6.27744
=====================================
root at: 
x = 4.96511423174643
Wien's constant b =  0.028990103307370348  m·K
=======================================
Inverse of A: [[-0.708, 2.531, 2.431, 0.967, -3.902], [-0.193, 0.31, 0.279, 0.058, -0.294], [0.022, 0.365, 0.286, 0.051, -0.29], [0.273, -0.13, 0.132, -0.141, 0.449], [0.782, -2.875, -2.679, -0.701, 4.234]]
=====================================
[1.4999972785141023, -0.49999999999977185, 1.9999999999999238, -2.499998638369165, 1.0000000000000913, -0.9999999997632304]
'''

