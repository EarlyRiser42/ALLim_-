import sys
import heapq

h = []
N = int(sys.stdin.readline())

for _ in range(N):
    heapq.heappush(h, int(sys.stdin.readline()))

ans = 0
memory = []
while h:
    if len(h) > 1:
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        ans = first + second
        memory.append(ans)
        heapq.heappush(h, ans)
    else:
        print(sum(memory))
        break

