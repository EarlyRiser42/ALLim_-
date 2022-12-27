from string import ascii_uppercase


def solution(m, n, board):
    answer = 0
    alpha = list(ascii_uppercase)
    for i in range(m):
        cash = set()
        for row in range(m - 1):
            for col in range(n - 1):
                if board[row][col] in alpha and board[row][col] == board[row][col + 1] == board[row + 1][col] == \
                        board[row + 1][col + 1]:
                    cash.add((row, col))
                    cash.add((row, col + 1))
                    cash.add((row + 1, col))
                    cash.add((row + 1, col + 1))
        answer += len(cash)
        if not cash:
            return answer
        for element in cash:
            board[element[0]] = board[element[0]][0:element[1]] + '0' +board[element[0]][element[1]+1:]
        [print(board[sex]) for sex in range(m)]
        print('************************')
        for row in range(m):
            for col in range(n):
                if board[row][col] == '0':
                    cash = row
                    for j in range(1, row+1):
                        if 0 <= row-j < m and board[row - j][col] in alpha:
                            board[cash] = board[cash][0:col] + board[row - j][col] + board[cash][col+1:]
                            board[row-j] = board[row-j][0:col] + '0' + board[row-j][col+1:]
                            cash = row - j
        [print(board[sex]) for sex in range(m)]
        print('----------------------------')
    return answer


print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))
