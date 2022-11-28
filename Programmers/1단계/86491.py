def solution(sizes):
    max_row, max_col = 1, 1
    row_i, col_i = 0,0
    for i in range(len(sizes)):
        if sizes[i][0] > max_row:
            max_row, row_i = sizes[i][0], i
        if sizes[i][1] > max_col:
            max_col, col_i = sizes[i][1], i
    if max_col < max_row:
        sizes[col_i][1] = sizes[col_i][0]
        cash = 1
        for ca in range(len(sizes)):
            if sizes[ca][1] > cash:
                cash = sizes[ca][1]
        answer = min(max_row*max_col, max_row*cash)
    elif max_col > max_row:
        sizes[col_i][0] = sizes[col_i][1]
        cash = 1
        for ca in range(len(sizes)):
            if sizes[ca][0] > cash:
                cash = sizes[ca][0]
        answer = min(max_row*max_col, max_row*cash)
    return answer


a = solution([[60, 50], [30, 70], [60, 30], [80, 40]])
print(a)
