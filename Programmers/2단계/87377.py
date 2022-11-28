from itertools import combinations


def get_gyojum(line1, line2):
    if line1[0] == line2[0]:
        return False
    elif line1[0] == 0:
        y = -line1[2]
        x = -line2[1] / line2[0]
        return (x, y)
    elif line2[0] == 0:
        y = -line2[2]
        x = -line1[1] / line1[0]
        return (x, y)
    elif line1[1] == 0:
        x = -line1[2]
        y = -line2[2] / line2[1]
        return (x, y)
    elif line2[1] == 0:
        x = -line2[2]
        y = -line1[2] / line1[1]
        return (x, y)
    else:
        A = -line2[0] / line1[0]
        y = (-A * line1[2] + line2[2]) / (A * line1[1] - line2[1])
        x = (-line1[2] - line1[0] * y) / line1[0]
        return (x, y)


def solution(line):
    answer = []
    line_com = list(combinations(line, 2))
    print(line_com)
    return answer