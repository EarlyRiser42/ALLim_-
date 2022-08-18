import sys

N = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start, end = 1, max(budget)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for money in budget:
        if money >= mid:
            cnt += mid
        else:
            cnt += money
    if cnt <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
