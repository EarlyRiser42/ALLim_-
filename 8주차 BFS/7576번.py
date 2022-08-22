import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(tomatoes):
    global cnt
    q = deque([tomatoes])
    while True:
        now = q.popleft()
        if len(now) == 0:
            break
        cache = []
        for cac in now:
            xx, yy = cac
            for i in range(4):
                nx = xx + dx[i]
                ny = yy + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    visited[nx][ny] = True
                    cache.append((nx, ny))
        q.append(cache)
        cnt += 1


M, N = map(int, sys.stdin.readline().split())
graph = []
tomato = []
cnt = 0
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[False]*M for __ in range(N)]

for row in range(N):
    for col in range(M):
        if graph[row][col] == 1:
            tomato.append((row, col))

bfs(tomato)

for row_ in range(N):
    if 0 in graph[row_]:
        print(-1)
        sys.exit(0)

print(cnt-1)

