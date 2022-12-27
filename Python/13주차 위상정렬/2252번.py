import sys


def dfs(n):
    visited[n] = True
    for child in tree[n]:
        if not visited[child]:
            dfs(child)
    rslt.append(n+1)


N, M = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N)]
visited = [False for __ in range(N)]
rslt = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    tree[a-1].append(b-1)

for i in range(N):
    if not visited[i]:
        dfs(i)

rslt.reverse()
[print(rslt[j], end=' ') for j in range(N)]
