#Pralhad GOverdhan Gadagi
#2311130
from mylibrary import *
#Question 1

A=readmatrix("matA.txt")
B=readmatrix("matB.txt")
def checksym(A):
    n = len(A)
    flag = True
    for i in range(n):
        for j in range(n):
            if A[i][j]!=A[j][i]: #checking here
                flag = False
            else:
                pass
    return flag
if checksym(A):
    x, lower = cholesky_decomp(A,B)
    print("cholesky : ", x)
else:
    print("Not symmetric")
x=guass_seidel(A,B)
print("guass seidel",x)


#question 2
print("======================================================")
A2=readmatrix("A.txt")
B2=readmatrix("B.txt")
x=jacobi(A2,B2,100)
x1=guass_seidel(A2,B2)
print("jacobi\n",x)
print("guass seidel\n",x1)
