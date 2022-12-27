import sys

N, Q = map(int, sys.stdin.readline().split())
B = [0]
B += list(map(int, sys.stdin.readline().split()))
B.sort()

for i in range(1, N+1):
    B[i] += B[i-1]

for j in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    print(B[R]-B[L-1])
