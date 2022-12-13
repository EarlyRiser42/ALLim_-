from copy import deepcopy
import sys
sys.setrecursionlimit(100000)


def dfs(x, y, maps, cnt):
    global answer
    maps[x][y] = 0
    cnt += 1
    if x == len(maps)-1 and y == len(maps[0])-1:
        if cnt < answer:
            answer = cnt
        return
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if 0 <= dx < len(maps) and 0 <= dy < len(maps[0]) and maps[dx][dy] == 1:
            map = deepcopy(maps)
            dfs(dx, dy, map, cnt)


def solution(maps):
    global answer
    answer = 10002
    dfs(0, 0, maps, 0)
    if answer == 10002:
        return -1
    else:
        return answer
