import sys

N = int(sys.stdin.readline())
dp = [0]*(N+1)
for i in range(1, N+1):
    list_ = list(map(int, sys.stdin.readline().split()))
    for child in list_[1:]:
        dp[i] = max(dp[i], dp[child]+list_[0])

print(max(dp))
