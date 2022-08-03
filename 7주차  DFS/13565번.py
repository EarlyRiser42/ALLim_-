import sys
sys.setrecursionlimit(1000000)


def dfs(x, y):
    visited[x][y] = True
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(nx, ny)


M, N = map(int, sys.stdin.readline().split())

graph = []
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[False]*N for i in range(M)]

for y in range(N):
    if graph[0][y] == 0 and not visited[0][y]:
        dfs(0, y)

if True in visited[M-1]:
    print('Yes')
else:
    print('No')
