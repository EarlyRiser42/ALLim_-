import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for tre in tree:
        if tre >= mid:
            cnt += tre - mid

    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
