import sys
from math import sin, copysign

A, B, C = list(map(int, sys.stdin.readline().split()))
sign = lambda x: copysign(1, x)


def f(x):
    return A*x + B*sin(x) - C


tol = 10**(-9)
start, end = 0, C

while start <= end:
    mid = (start+end) / 2
    if f(mid) == 0 or (end - start) < tol:
        print(mid)
        sys.exit(0)
    if sign(mid) == sign(start):
        start = mid + 1
    else:
        end = mid - 1
print(end, start)
print(end-start)
print(mid)
