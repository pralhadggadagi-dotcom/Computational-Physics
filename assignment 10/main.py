#pralhad Goverdhan Gadagi
#2311130
from mylibrary import *
import math as m
def f1(x):
    return 1/x

def f2(x):
    return x*m.cos(x)
def f3(x):
    return x*m.atan(x)

N = [4, 8, 15, 20]

for n in N:
    print("\n=========================================================")
    print("For N =", n)

    m1 = midpoint(1, 2, f1, n)
    m2 = midpoint(0, m.pi/2, f2, n)
    m3 = midpoint(0, 1, f3, n)

    t1 = trapezoidal(1, 2, f1, n)
    t2 = trapezoidal(0, m.pi/2, f2, n)
    t3 = trapezoidal(0, 1, f3, n)
    print("for function 1")
    print("midpoint", m1)
    print("trapezoidal",t1)
    print("analytic result", m.log(2))
    print("for function 2")
    print("midpoint", m2)
    print("trapezoidal",t2)
    print("analytic result",(m.pi/2) - 1 )
    print("for function 3")
    print("midpoint", m3)
    print("trapezoidal",t3)
    print("analytic result", (m.pi/4) - 0.5)

"""
output


Function	Exact Result	Midpoint N=4	Midpoint N=8	Midpoint N=15	Midpoint N=20	Trap N=4	Trap N=8	Trap N=15	   Trap N=20
1/x	          0.69314718	0.691219891	    0.692660554	    0.693008426	    0.693069098	   0.563095238	0.629538517	 0.659516758   0.667982869
x*cos(x)	  0.570796327	0.587447917	    0.574934273	    0.571971659	    0.571457287	   0.449085235	0.536202815	 0.560422255   0.564876824
x*arctan(x)	  0.285398163	0.282046049	    0.284561019	    0.285160103	    0.28526426	   0.133595347	0.198673797	 0.236332088   0.247986644

=========================================================
For N = 4
for function 1
midpoint 0.6912198912198912
trapezoidal 0.6970238095238095
analytic result 0.6931471805599453
for function 2
midpoint 0.5874479167573121
trapezoidal 0.5376071275673585
analytic result 0.5707963267948966
for function 3
midpoint 0.2820460493571144
trapezoidal 0.29209834589395167
analytic result 0.2853981633974483

=========================================================
For N = 8
for function 1
midpoint 0.6926605540432034
trapezoidal 0.6941218503718504
analytic result 0.6931471805599453
for function 2
midpoint 0.574934273382131
trapezoidal 0.5625275221623354
analytic result 0.5707963267948966
for function 3
midpoint 0.2845610193056679
trapezoidal 0.28707219762553304
analytic result 0.2853981633974483

=========================================================
For N = 15
for function 1
midpoint 0.6930084263712957
trapezoidal 0.6934248043580646
analytic result 0.6931471805599453
for function 2
midpoint 0.5719716590967574
trapezoidal 0.5684462350385163
analytic result 0.5707963267948966
for function 3
midpoint 0.28516010270349235
trapezoidal 0.2858742642174127
analytic result 0.2853981633974483

=========================================================
For N = 20
for function 1
midpoint 0.6930690982255869
trapezoidal 0.693303381792694
analytic result 0.6931471805599453
for function 2
midpoint 0.5714572867152206
trapezoidal 0.569474588169518
analytic result 0.5707963267948966
for function 3
midpoint 0.2852642601614453
trapezoidal 0.285665963360493
analytic result 0.2853981633974483
"""