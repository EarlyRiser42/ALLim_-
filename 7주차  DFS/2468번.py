import sys
sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    visited[x][y] = True
    for __ in range(4):
        nx = x + dx[__]
        ny = y + dy[__]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > min_ and not visited[nx][ny]:
            dfs(nx, ny)


N = int(sys.stdin.readline())

ans = []
graph = []

input_ = list(map(int, sys.stdin.readline().split()))
graph.append(input_)
min_list = set(input_)

for _ in range(N-1):
    input_ = list(map(int, sys.stdin.readline().split()))
    graph.append(input_)
    min_list.update(input_)

visited = [[False]*N for i in range(N)]

for min_ in range(max(map(max, graph))):
    print(min_)
    land_num = 0
    for alpha in range(N):
        for beta in range(N):
            if graph[alpha][beta] > min_ and not visited[alpha][beta]:
                land_num += 1
                dfs(alpha, beta)
    visited = [[False] * N for i in range(N)]
    ans.append(land_num)

land_num = max(ans)
print(land_num)
