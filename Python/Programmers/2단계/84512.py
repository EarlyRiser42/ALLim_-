from itertools import product

def solution(word):
    dic = []
    for i in range(1,6):
        permutation = product(['A','E','I','O','U'], repeat=i)
        for permu in permutation:
            dic.append(''.join(permu))
    dic.sort()
    answer = dic.index(word)+1
    return answer