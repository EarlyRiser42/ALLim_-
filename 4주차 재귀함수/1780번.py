import math


def diva(n,x, y, r, o, one, mone, zero):
    if [[board[i][z] for i in range(x, y+1)]for z in range(r, o+1)] == 0:
        zero += 1
        return 1
    if [[board[i][z] for i in range(x, y+1)]for z in range(r, o+1)] == 1:
        one += 1
        return 1
    if [[board[i][z] for i in range(x, y+1)]for z in range(r, o+1)] == -1:
        mone += 1
        return 1

    w = math.floor(y/3)
    q = w-(math.floor(y/3))
    k = math.log(n,3)
    return diva(n, q, w, q, w, one, mone, zero), diva(n, q, w+k, q, w, one, mone, zero), diva(n, q, w, q, w+k, one, mone, zero), diva(n, q, w+k, q, w+k, one, mone, zero), diva(n, q, w+2*k, q, w, one, mone, zero), diva(n, q, w, q, w+2*k, one, mone, zero), diva(n, q, w+k, q, w+2*k, one, mone, zero), diva(n, q, w+2*k, q, w+k, one, mone, zero), diva(n, q, w+2*k, q, w+2*k, one, mone, zero),


x = int(input())
board = [[0 for col in range(x)] for row in range(x)]
board = [[int(x) for x in input().split()] for _ in range(x)]
y = x-1
one = mone = zero = 0
ans = []
diva(x,y, y, y, y, one, mone, zero)
print(one, mone, zero)
