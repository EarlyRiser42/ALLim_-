import sys


def dfs(n):

    for i in tree[n]:
        if par[i] == 0:
            par[i] = n
            print(i, n, par[1:])
            dfs(i)


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
tree = [[] for _ in range(n + 1)]

par = [0] * (n + 1)


for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
for i in range(2, n + 1):
    print(par[i])
