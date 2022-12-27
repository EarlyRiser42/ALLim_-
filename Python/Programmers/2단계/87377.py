def solution(line):
    gyojum_list = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a * d - b * c != 0:
                x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    if (x, y) not in gyojum_list:
                        gyojum_list.append((x, y))
    print(max(gyojum_list))
    x_min, x_max, y_min, y_max = min(gyojum_list)[0], max(gyojum_list)[0], min(gyojum_list, key=lambda x: x[1])[1], \
                                 max(gyojum_list, key=lambda x: x[1])[1]

    board = [['.']*(abs(x_max-x_min)+1) for _ in range((abs(y_max-y_min)+1))]

    for gyojums in gyojum_list:
        x, y = abs(y_max - int(gyojums[1])), abs(x_min - int(gyojums[0]))
        board[x][y] = '*'
    for i, v in enumerate(board):
        board[i] = ''.join(v)
    return board

