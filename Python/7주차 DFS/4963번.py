import sys
sys.setrecursionlimit(10000)


def path_find(x,y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    array[x][y] = True
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < row and 0 <= ny < col and ma_p[nx][ny] == 1 and not array[nx][ny]:
            path_find(nx, ny)


while True:
    col, row = map(int, sys.stdin.readline().split())
    if row == 0 and col == 0:
        break
    ma_p = []
    count = 0
    for i in range(row):
        inputs = list(map(int, sys.stdin.readline().split()))
        ma_p.append(inputs)

    array = [[False for sex in range(col)] for sexs in range(row)]

    for x in range(row):
        for y in range(col):
            if ma_p[x][y] == 1 and not array[x][y]:
                path_find(x, y)
                count += 1

    print(count)
