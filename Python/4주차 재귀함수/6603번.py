from itertools import combinations


def ina():  # 입력을 받아 2차원 배열에 저장
    a = list(map(int, input().split()))
    if int(a[0]) == 0:
        return 1
    if int(a[0])+1 == len(a):
        b.append(a)
        return ina()


def sel(r):
    g = b[r][1:]
    ans = (list(combinations(g, 6)))
    for i in range(len(ans)):
        for u in range(len(ans[0])):
            print(ans[i][u], end=' ')
        if i != len(ans)-1:
            print(end='\n')
    if r == len(b)-1:
        return 1
    return print(end='\n\n'), sel(r+1)


b = []
ina()
r = 0
sel(r)
