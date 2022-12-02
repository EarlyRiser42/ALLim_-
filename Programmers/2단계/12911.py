def solution(n):
    count = bin(n).count('1')
    for i in range(n+1,2*n):
        if bin(i).count('1') == count:
            return i