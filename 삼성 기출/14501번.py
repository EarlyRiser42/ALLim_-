N = int(input())
T, P = [], []
for i in range(N):
    T_pre, P_pre = map(int, input().split())
    if T_pre+i <= N:
        T.append(T_pre)
        P.append(P_pre)

dp = [0 for _ in range(len(T))]

for j in range(len(T)):
    dp[j] = max(dp[j], P[j] + dp[j+T[j]])

print(dp[-1])
