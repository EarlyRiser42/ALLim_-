import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    tree = [[] for tre in range(N)]
    in_degree = [0]*N
    dp = [0 for d in range(N)]
    result = []
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        tree[X-1].append(Y-1)
        in_degree[Y-1] += 1
    stop = int(sys.stdin.readline())
    queue = deque()
    for k in range(N):
        if in_degree[k] == 0:
            queue.append(k)
            dp[k] = time[k]  # 부모 노드 dp 채움 (부모 노드부터 시작 하기에)
    while len(queue) > 0:
        now = queue.popleft()
        result.append(now)
        for child in tree[now]:
            in_degree[child] -= 1
            dp[child] = max(dp[now] + time[child], dp[child])
            if in_degree[child] == 0:
                queue.append(child)

    print((dp[stop-1]))


