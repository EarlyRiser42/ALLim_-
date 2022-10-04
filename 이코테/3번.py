S = str(input())

ans_max = float('inf')

for small in ('0', '1'):
    cnt, ans = 0, 0
    for i in range(len(S)):
        if S[i] == small:
            cnt = 1
        elif cnt == 1 and S[i] != small:
            ans += 1
            cnt = 0
    if cnt == 1:
        ans += 1

    ans_max = min(ans_max, ans)

print(ans_max)
