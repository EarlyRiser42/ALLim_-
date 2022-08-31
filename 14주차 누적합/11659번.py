import sys

N, M = map(int, sys.stdin.readline().split())

S = [0]
S += list(map(int, sys.stdin.readline().split()))

for i in range(1, N+1):
    S[i] += S[i-1]  # 누적합 돌리기

for j in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(S[b]-S[a-1])
