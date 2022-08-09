import sys


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < N and 0 <= w < M and graph[q][w] == 1:
                graph[q][w] = 0
                queue.append([q, w])


T = int(input())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _y in range(N)]
    cnt = 0
    for k in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1:
                bfs(row, col)
                graph[row][col] = 0
                cnt += 1
    print(cnt)
