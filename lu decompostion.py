#Pralhad Goverdhan Gadagi
#2311130

from mylibrary import *
mat1=readmatrix("matA.txt")
L,U,A=lu_decom1(mat1)
print("lower", L)
print("upper", U)
print("A",A)
print("varified",matmulti(L,U))

"""
lower [[1, 0, 0], [3.0, 1, 0], [2.0, 1.0, 1]]
upper [[1.0, 2.0, 4.0], [0, 2.0, 2.0], [0, 0, 3.0]]
A [[1, 2.0, 4.0], [3.0, 1, 2.0], [2.0, 1.0, 1]]
varified [[1.0, 2.0, 4.0], [3.0, 8.0, 14.0], [2.0, 6.0, 13.0]]
"""

#question 2
a = readmatrix('vecA.txt')
b = readmatrix('vecB.txt')

sol = solution(a, b)
print("Solution of the equation:", sol)
 """
indexing error
 """

