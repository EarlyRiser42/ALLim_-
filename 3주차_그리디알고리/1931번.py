from operator import itemgetter

num = int(input())  # 세로 길이 설정
board = [[int(x) for x in input().split()]for y in range(num)]
ans = []

board.sort(key=itemgetter(1), reverse=False)

i = 0

for y in range(num):
    if board[i][1] < board[y][0]:
        ans.append(board[i])
        i = y

if len(ans) == 0:
    ans.append(board[0])

if board[num-1][0] > ans[len(ans)-1][1]:
    ans.append(board[num-1])

print(len(ans))
