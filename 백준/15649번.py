from math import factorial
from collections import deque


def recursion(i):
    cash = []
    for j in range(M):
        while len(cash) == N:
            cash.append(candidate[j])
        ans.append(cash)


M, N = map(int, (input().split()))

ans = []
candidate = list(range(1, M+1))

length = factorial(M)//factorial((M-N))
