import sys

N, H = map(int, sys.stdin.readline().split())
obstacles = []
for _ in range(N):
    obstacles.append(int(sys.stdin.readline()))

start, end = 1, H

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(N):
        if i % 2 != 0 and obstacles[i] > mid:  # 홀수(0, 1, 3..)
            cnt += 1
        elif i % 2 == 0 and obstacles[i] < mid:
            cnt += 1
    if cnt