import sys

K, N = map(int, sys.stdin.readline().split())
wires = []
for i in range(K):
    wires.append(int(sys.stdin.readline()))

start, end = 1, max(wires)

while start <= end:
    cnt = 0
    mid = (start+end) // 2
    for wire in wires:
        cnt += (wire // mid)
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
