import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewelry = []
bags = []

for _ in range(N):
    heapq.heappush(jewelry, list(map(int, sys.stdin.readline().split())))

for __ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

ans = 0
tmp_jew = []

for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jewelry)[1])
    if tmp_jew:
        ans -= heapq.heappop(tmp_jew)
    elif not jewelry:
        break

print(ans)
