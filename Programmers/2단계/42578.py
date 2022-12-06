def solution(clothes):
    dic = {}
    for cloth in clothes:
        dic[cloth[1]] = 1
    for cloth in clothes:
        dic[cloth[1]] += 1
    answer = 1
    for key in list(dic.keys()):
        answer *= dic[key]
    return answer-1