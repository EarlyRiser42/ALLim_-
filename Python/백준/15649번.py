from copy import deepcopy
from math import factorial


def recursion(i):
    global cash
    for j in range(1, M+1):
        cash.append(j)
        if i > 1:
            recursion(i-1)
        if len(cash) == N:
            if cash not in ans:
                cashh = deepcopy(cash)
                ans.append(cashh)
            cash.pop()
    cash = []
    return ans


M, N = map(int, input().split())
ans = []
cash = []
rslt = recursion(N)
[print(rslt[_]) for _ in range(len(rslt))]