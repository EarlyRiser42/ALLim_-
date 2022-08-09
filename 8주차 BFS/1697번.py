import sys
from collections import deque


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == K:
            return array[v]
        for next_v in (2*v, v-1, v+1):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


N, K = map(int, sys.stdin.readline().split())

MAX = 100001
array = [0] * MAX

print(bfs(N))
