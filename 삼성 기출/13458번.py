N = int(input())
A_list = list(map(int, input().split()))
B, C = map(int, input().split())

left = []
for i in range(N):
    left.append(A_list[i] - B)

cnt = 0

for j in range(N):
    if left[j] > 0:
        ans, stan = divmod(left[j], C)
        if stan == 0:
            cnt += ans
        else:
            cnt += ans + 1

print(N+cnt)
