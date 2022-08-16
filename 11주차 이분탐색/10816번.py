import sys

N = int(sys.stdin.readline())
own_card = list(map(int, sys.stdin.readline().split()))
own_card.sort()

M = int(sys.stdin.readline())
how_many = list(map(int, sys.stdin.readline().split()))

ans = []

for i in range(M):
    cnt = 0
    target = how_many[i]
    left, right = 0, N-1
    mid = (left + right) // 2
    while left < right:
        mid = (left+right) // 2
        if own_card[mid] == target:
            left = right = mid
        elif own_card[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    standard_right, standard_left = mid, mid
    if own_card[mid] == how_many[i]:
        cnt += 1
    while 0 <= standard_left - 1 < N and own_card[standard_left - 1] == how_many[i]:
        cnt += 1
        standard_left -= 1
    while 0 <= standard_right + 1 < N and own_card[standard_right + 1] == how_many[i]:
        cnt += 1
        standard_right += 1
    ans.append(cnt)

print(*ans)
