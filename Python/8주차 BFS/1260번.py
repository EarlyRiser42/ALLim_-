import sys
from collections import deque


def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in tree[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in tree[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


N, M, V = map(int, sys.stdin.readline().strip().split())
tree = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
for i in range(len(tree)):
    tree[i].sort()

dfs(V)
visited = [False]*(N+1)
print()
bfs(V)
