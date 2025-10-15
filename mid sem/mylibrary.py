import math
import matplotlib.pyplot as plt
def simpson(a ,b,f,n):
    h= (b -a ) / n
    total = (f(a) + f(b))
    for i in range(1,n):
        if i % 2 ==0:
            total += 2 * f(a + i * h)
        else:
            total += 4 * f(a + i * h)
    return h * (total) / 3
def montecarlo(a,b,f,n):
    start = LCGrandom()
    total=0
    totalvar=0
    xaxis = []
    yaxis = []
    varaxis = []
    for i in range(n):
        small= start.generate()
        xi=a + small * ( b - a )
        fxi= f(xi)
        totalvar += fxi**2
        total +=   fxi
        if i % 100 ==0  and i !=0:
            mean = total / i
            var = totalvar / i - mean**2
            yaxis.append(mean * (b - a))
            varaxis.append(var)
            xaxis.append(i)


    mean= total / n
    var= totalvar/n -mean**2
    return mean * (b - a) ,var , xaxis,yaxis,varaxis


def midpoint( a, b,f, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        total += f(x_mid)
    return total * h

def trapezoidal( a, b,f, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

def newton_raphson(f,df,accu,x,itrations ):
    global i
    for i in range (itrations):
        x1=x - f(x)/df(x)
        if abs(x1-x) < accu:
            print("root at: ")
            return x1
        x=x1
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
def regula_falsi(a,b,accu,f,cprev=None):
    c = b - ((b - a) * f(b)) / (f(b) - f(a))
    if cprev is not None and abs(cprev-c) < accu :
        return c

    if f(a)*f(c) < 0:
        a,b=a,c
    if f(b)*f(c) < 0:
        a,b=c,b

    return regula_falsi(a,b,accu ,f,c)
def bracketing(a,b,f):
    if f(a)*f(b) < 0 :
        return a,b
    if abs(f(a)) < abs(f(b)) :
        a= a - 0.1*(b-a)
    else:
        b=b + 0.1*(b-a)
    return bracketing(a,b,f)
def guass_seidel(A,B):
    n = len(A)
    x = [0.0] * n
    #step 1: to check itratively
    for itration in range(100):
        xnew = x.copy()
        for i in range(n):
            #solving first sumation
            sum = 0
            for j in range(i):
                sum = sum + A[i][j] * xnew[j]
            # solving second sumation
            suma = 0
            for j in range(i + 1, n):
                suma = suma + A[i][j] * x[j]
            #using eqation
            xnew[i] = (B[i][0] - sum - suma) / A[i][i]

        err = 0
        for i in range(n):
            if abs(xnew[i] - x[i]) > err:
                err = abs(xnew[i] - x[i])
    #step 2: check for threshold/convergence
        if err < 10e-6:
            return xnew
        x = xnew
def cholesky_decomp(A, B):
    n = len(A)
    lower = [[0.0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            sum_val = 0
            for k in range(j):
                sum_val += lower[i][k] * lower[j][k]

            if i == j:
                lower[i][i] = math.sqrt(A[i][i] - sum_val)
            else:
                lower[i][j] = (A[i][j] - sum_val) / lower[j][j]

    y = [0.0] * n
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += lower[i][j] * y[j]
        y[i] = (B[i][0] - sum) / lower[i][i]
    x = [0.0] * n
    for i in reversed(range(n)):
        suma = 0
        for j in range(i+1, n):
            suma += lower[j][i] * x[j]
        x[i] = (y[i] - suma) / lower[i][i]

    return x, lower

def jacobi(A, B, itration):
    n = len(A)
    x=[0]*n
    for something in range(itration):
        xnew=[0]*n
        for i in range(n):
            sum = 0
            for j in range(n):
                if i!= j:
                   sum = sum +  A[i][j]*x[j]
            xnew[i] = (B[i][0] - sum)/A[i][i]
        x= xnew
    return x
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
def ludecompsolution(A, B):
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
def lu_solve(L, U, b):
    n = len(L)
    y = [0.0 for _ in range(n)]
    x = [0.0 for _ in range(n)]

    # Forward substitution: L*y = b
    for i in range(n):
        sumy = 0
        for j in range(i):
            sumy += L[i][j] * y[j]
        y[i] = b[i] - sumy

    # Backward substitution: U*x = y
    for i in range(n-1, -1, -1):
        sumx = 0
        for j in range(i+1, n):
            sumx += U[i][j] * x[j]
        x[i] = (y[i] - sumx) / U[i][i]

    return x
class LCGrandom():
    def __init__(self):
        self.a = 1103515245
        self.m=32768
        self.c = 12345
        self.x=1

    def generate(self):
        self.x=((self.a*self.x+ self.c))% self.m
        return self.x/(self.m - 1)

class Plots():
    def _init_(self):
        pass

    def plot(self,x, y,title,xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.scatter(x, y, marker='o', color='b')
        plt.grid(True)
        plt.show()
        #plt.savefig(f"{title}.png")

    def line_plot(self,x, y,title,xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.plot(x, y)
        plt.grid(True)
        plt.show()
        #plt.savefig(f"{title}.png")

    def hist(self, data, title, xlabel, ylabel, bins):
        plt.hist(data, bins=bins, color='skyblue', edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
def gaussjordan_inverse(A):
    n = len(A)
    augment = []
    for i in range(n):
        row = []

        for j in range(n):
            row.append(A[i][j])

        for j in range(n):
            if i == j:
                row.append(1.0)
            else:
                row.append(0.0)
        augment.append(row)

    for i in range(n):

        if augment[i][i] == 0:
            for k in range(i+1, n):
                if augment[k][i] != 0:
                    augment[i], augment[k] = augment[k], augment[i]
                    break

        diag = augment[i][i]
        for j in range(2*n):
            augment[i][j] = augment[i][j] / diag

        for k in range(n):
            if k != i:
                factor = augment[k][i]
                for j in range(2*n):
                    augment[k][j] -= factor * augment[i][j]

    inverse = []
    for i in range(n):
        row = []
        for j in range(n, 2*n):
            row.append(augment[i][j])
        inverse.append(row)

    return inverse


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
    m = len(B)
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