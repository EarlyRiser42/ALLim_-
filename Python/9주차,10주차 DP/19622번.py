import sys

n = int(sys.stdin.readline())

times = []
for _ in range(n):
    times.append(list(map(int, sys.stdin.readline().split())))


dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = times[i][2]
    elif i == 1:
        dp[i] = max(times[i][2], dp[i-1])
    else:
        dp[i] = max(dp[i-2] + times[i][2], dp[i-1])

print(dp[n-1])
