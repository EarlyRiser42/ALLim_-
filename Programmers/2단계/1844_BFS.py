from collections import deque


def bfs(x,y, maps, cnt):
    maps[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([(x,y)])
    while queue:
        cash = queue.popleft()
        for i in range(4):
            nx = cash[0] + dx[i]
            ny = cash[1] + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                [print(maps[k]) for k in range(len(maps))]
                print('-----------------------')
                maps[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt


def solution(maps):

    answer = bfs(0,0, maps, 1)
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
