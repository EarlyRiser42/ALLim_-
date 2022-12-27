def solution(board):
    answer = 0
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    # 첫열과 행을 미리 셋팅하는 부분
    dp[0] = board[0]
    for row in range(len(board)):
        dp[row][0] = board[row][0]

    for row in range(0, len(dp)):
        for col in range(0, len(dp[0])):
            # 첫열과 첫행 부분은 넘기며, 현재 블록 값이 1인 경우에만 계산
            if (row - 1 >= 0) and (col - 1 >= 0) and board[row][col] == 1:
                dp[row][col] = min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]) + 1

    for i in range(len(dp)):
        temp = max(dp[i])
        answer = max(answer, temp)

    # 앞의 행의 가잗큰값만을 뽑아오므로 이렇게하면안됨
    # answer = max(max(max(dp)),answer)
    return answer * answer