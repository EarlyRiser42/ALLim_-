def convert(n):
    count = n.count('0')
    binary = len(n)-count
    return bin(binary)[2:], count


def solution(s):
    cash = 0
    i = 0
    while s != '1':
        a, b = convert(s)
        s = a
        cash += b
        i += 1
    answer = [i,cash]
    return answer