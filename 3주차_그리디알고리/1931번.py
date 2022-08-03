import sys

num = int(sys.stdin.readline())  # 세로 길이 설정
board_pre = []
for _ in range(num):
    board_pre.append(list(map(int, sys.stdin.readline().split())))

ans = 1

board = sorted(board_pre, key=lambda x: (x[1], x[0]))

max_ = board[0][1]

for i in range(1, num):
    if board[i][0] >= max_:
        ans += 1
        max_ = board[i][1]

print(ans)
