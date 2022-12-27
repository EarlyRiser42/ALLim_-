import sys
from bisect import bisect_left

N, H = map(int, sys.stdin.readline().split())
obstacles_top = []
obstacles_bot = []

for i in range(N):
    if i % 2 == 0:
        obstacles_bot.append(int(sys.stdin.readline()))
    else:
        obstacles_top.append(int(sys.stdin.readline()))

obstacles_top.sort()
obstacles_bot.sort()

start, end = 1, H
cnt = 1
min_val = N

# bisect 로 완전 탐색 + 이분 탐색
for h in range(1, H+1):
    t, b = bisect_left(obstacles_top, (H+1)-h), bisect_left(obstacles_bot, h)
    total = N - (t+b)
    if total < min_val:
        min_val = total
        cnt = 1
    elif total == min_val:
        cnt += 1

print(min_val, cnt)
