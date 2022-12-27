n = int(input())
series = list(map(int, input().split()))
dp = [0] * len(series)
dp[0] = series[0]

for i in range(1, len(series)):
    dp[i] = max(series[i], dp[i-1] + series[i])

print(max(dp))