import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x, y):
    visited[x][y] = True
    for __ in range(4):
        nx = x + dx[__]
        ny = y + dy[__]
        if graph[nx][ny] > min_ and not visited[nx][ny]:
            dfs(nx, ny)


land_num = 0
N = int(sys.stdin.readline())

graph = []

input_ = list(map(int, sys.stdin.readline().split()))
min_ = min(input_)
graph.append(input_)

for _ in range(N-1):
    input_ = list(map(int, sys.stdin.readline().split()))
    min_ = min(input_)
    if min(input_) < min_:
        min_ = min(input_)
    graph.append(input_)

visited = [False for i in range(N)]

for alpha in range(N):
    for beta in range(N):
        if graph[alpha][beta] > min_ and not visited[alpha][beta]:
            dfs(alpha, beta)
            land_num += 1
