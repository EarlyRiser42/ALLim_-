from bisect import bisect_left, bisect_right
import sys

N = int(sys.stdin.readline())
own_card = list(map(int, sys.stdin.readline().split()))
own_card.sort()

M = int(sys.stdin.readline())
how_many = list(map(int, sys.stdin.readline().split()))

ans = []

for i in range(M):
    cnt = bisect_right(own_card, how_many[i]) - bisect_left(own_card, how_many[i])
    ans.append(cnt)

print(*ans)
