import sys
from math import sin, copysign

A, B, C = list(map(int, sys.stdin.readline().split()))
sign = lambda x: copysign(1, x)


def f(x):
    return A*x + B*sin(x) - C


tol = 10**(-9)
start, end = 0, 2*C

while abs(start-end) > tol:
    mid = (start+end) / 2
<<<<<<< HEAD
    if sign(f(start)) != sign(f(mid)):
        end = mid
    elif sign(f(end)) != sign(f(mid)):
        start = mid
=======
    if f(mid) <= 0:
        start = mid
    else:
        end = mid
>>>>>>> 023d4bee7adb8c47f0f34ec8b388c7ddc19978c5

print(mid)
