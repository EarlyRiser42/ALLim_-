from itertools import combinations



def sel(r):
    ans = (list(combinations(b, y)))
    for i in range(len(ans)):
        for u in range(len(ans[0])):
            print(ans[i][u], end=' ')
        if i != len(ans)-1:
            print(end='\n')
    if r == len(b)-1:
        return 1


x, y = map(int, input().split())
b = [0]*x
r = 0
for i in range(x):
    b[x-i-1] = x-i
sel(r)

