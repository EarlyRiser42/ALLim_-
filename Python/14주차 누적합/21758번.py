import sys
from copy import deepcopy
N = int(sys.stdin.readline())

input_ = list(map(int, sys.stdin.readline().split()))
H = input_  # 원본 배열
S = deepcopy(input_)  # 누적합 배열
result = 0

for i in range(1, N):
    S[i] += S[i - 1]

for i in range(1, N - 1):  # 오른쪽
    result = max(result, 2 * S[-1] - H[0] - H[i] - S[i])

for i in range(1, N - 1):  # 왼쪽
    result = max(result, S[-1] - H[-1] - H[i] + S[i - 1])
for i in range(1, N - 1):  # 중간
    result = max(result, S[i] - H[0] + S[-1] - S[i - 1] - H[-1])

print(result)

