import sys


def dfs(n):
    visited[n] = True
    cycle.add(n)
    for child in tree[n]:
        if child in cycle:
            print(0)
            sys.exit(0)
        if not visited[child]:
            dfs(child)
    rslt.append(n+1)
    cycle.remove(n)


N, M = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N)]
visited = [False for __ in range(N)]
rslt = []

for _ in range(M):
    list_ = list(map(int, sys.stdin.readline().split()))
    for i in range(list_[0]-1):
        tree[list_[i+1]-1].append(list_[i+2]-1)

for j in range(N):
    if not visited[j]:
        cycle = set()
        dfs(j)

rslt.reverse()

for k in rslt:
    print(k)
