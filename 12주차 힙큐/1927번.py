import sys
import heapq

N = int(sys.stdin.readline())
h = []

for i in range(N):
    input_ = int(sys.stdin.readline())
    if input_ == 0:
        if len(h) == 0:
            print(0)
        else:
            pop = heapq.heappop(h)
            print(pop)
    else:
        heapq.heappush(h, input_)
