def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        row, col = divmod(i,n)
        if col > row:
            answer.append(col+1)
        else:
            answer.append(row+1)
    return answer