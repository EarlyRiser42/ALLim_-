import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global cnt
    graph[x][y] = 0
    q = deque([(x, y)])
    while q:
        now = q.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))


N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))
ans = []

for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            cnt = 1
            bfs(x, y)
            ans.append(cnt)
ans.sort()
print(len(ans))
[print(ans[k]) for k in range(len(ans))]
