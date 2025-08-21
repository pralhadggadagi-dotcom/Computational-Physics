
def lu_decom1(A):
    n = len(A)
    lower = []
    upper = []
    for i in range(n):
        lower.append([0]*n)
        upper.append([0]*n)
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum = sum + lower[i][k] * upper[k][j]
            upper[i][j] = A[i][j] - sum
        for j in range(i, n):
            if i == j:
                lower[i][i] = 1
            else:
                sum = 0
                for k in range(i):
                    sum = sum + lower[j][k] * upper[k][i]
                lower[j][i] = (A[j][i] - sum) / upper[i][i]
    for i in range( n):
        for j in range( n):
            if i <= j:
                A[i][j] = upper[i][j]
            elif i > j:
                A[i][j] = lower[i][j]
            else:
                A[i][j]=1
    return lower,upper,A
def solution(A, B):
    n = len(A)
    L, U = lu_decom(A)

    y = [0.0] * n
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]
        y[i] = B[i][0] - sum

    x = [0.0] * n
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += U[i][j] * x[j]
        x[i] = (y[i] - sum) / U[i][i]

    return x

def lu_decom(A):
    n = len(A)
    lower = []
    upper = []
    for i in range(n):
        lower.append([0]*n)
        upper.append([0]*n)
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum = sum + lower[i][k] * upper[k][j]
            upper[i][j] = A[i][j] - sum
        for j in range(i, n):
            if i == j:
                lower[i][i] = 1
            else:
                sum = 0
                for k in range(i):
                    sum = sum + lower[j][k] * upper[k][i]
                lower[j][i] = (A[j][i] - sum) / upper[i][i]
    return lower,upper

class LCGrandom():
    def __init__(self):
        self.a = 1103515245
        self.m=32768
        self.c = 12345
        self.x=1

    def generate(self):
        self.x=((self.a*self.x+ self.c))% self.m
        return self.x/(self.m - 1)

def gaussjordan(veca, vecb):

    for i in range(len(veca)):
        veca[i].append(vecb[i])
    augment = veca
    n = len(augment)
    for i in range(n):
        if augment[0][0] < augment[i][0]:
            augment[0],augment[i]=augment[i],augment[0]
        if augment[i][i] == 0:
            for k in range(i+1, n):
                if augment[k][i] != 0:
                    augment[i], augment[k] = augment[k], augment[i]
                    break
        diagonal = augment[i][i]
        if diagonal == 0:
            return ("error")

        for j in range(i, n+1):
            augment[i][j] = augment[i][j] / diagonal

        for k in range(n):
            if k != i:
                multi = augment[k][i]
                for j in range(i, n+1):
                    augment[k][j] -= multi * augment[i][j]
    solution=[]
    for i in range(n):
        solution.append(augment[i][-1])
    return solution

def matmulti(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            val = 0
            for k in range(p):
                val = val + A[i][k] * B[k][j]
            row.append(val)
        result.append(row)
    return result

def readmatrix(filename):
    with open(filename, "r" ) as f :
        matrix = []
        for line in f:
            # S p l i t t h e l i n e i n t o numbers and c o n v e r t t o i n t / f l o a t
            row = [float(num) for num in line.strip().split()]
            matrix.append(row)

    return matrix

def getLU(A):
    n = len(A)
    lower = []
    upper = []
    for i in range(n):
        row1 = []
        row2 = []
        for j in range(n):
            row1.append(0)
            row2.append(0)
        lower.append(row1)
        upper.append(row2)
    for i in range(n):
        for j in range(n):
            if i==j:
                lower.append(1.0)
    for i in range(n):
        for j in range(n):
            if i <= j:
                upper[i][j] = A[i][j]
            elif i > j:
                lower[i][j] = A[i][j]
    return lower , upper