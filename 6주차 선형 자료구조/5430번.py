import sys
from collections import deque

T = int(sys.stdin.readline())
p = \
    []
n = []
xn = []

for i in range(T):
    p.append(list(sys.stdin.readline().rstrip()))
    n.append(int(sys.stdin.readline()))
    if n[i] == 0:
        xn.append(deque())
        continue
    xn.append(deque(sys.stdin.readline().rstrip()[1:-1].split(",")))

for x in range(T):
    error_cnt = 0
    for y in p[x]:
        if y == 'R':
            xn[x].reverse()
        else:
            try:
                xn[x].popleft()
            except:
                print('error')
                error_cnt += 1
                break
    if error_cnt == 0:
        que = ''
        for k in range(len(xn[x])):
            que += str(xn[x][k]) + ','
        print(f'[{que[:-1]}]')
