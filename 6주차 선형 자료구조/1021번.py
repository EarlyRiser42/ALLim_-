import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))

list_pre = list(range(1, N+1))
que = deque(list_pre)
cnt = 0
while len(que) > N-M:
    for x in range(M):
        if que.index(location[x]) > len(que)/2:
            while que[0] != location[x]:
                y = que.pop()
                que.appendleft(y)
                cnt += 1
            que.popleft()

        else:
            while que[0] != location[x]:
                z = que.popleft()
                que.append(z)
                cnt += 1
            que.popleft()
print(cnt)
