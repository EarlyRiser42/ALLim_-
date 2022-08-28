import sys
from bisect import bisect_left

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
left = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    tree[a-1].append(b-1)

for j in range(N):
    if not visited[N-j-1] and tree[N-j-1]:
        dfs(N-j-1)
for k in range(N):
    if not visited[N-k-1]:
        left.append(N-k)

rslt.reverse()
for g in (left):
    b = bisect_left(rslt, g)
    rslt.insert(b, g)

[print(k, end=' ') for k in rslt]

