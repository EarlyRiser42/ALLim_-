import sys

N, Q = map(int, sys.stdin.readline().split())
L = [0] + list(map(int, sys.stdin.readline().split()))
for _ in range(Q):
    l, r = map(int, sys.stdin.readline().split())
    