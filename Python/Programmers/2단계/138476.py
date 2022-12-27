def solution(k, tangerine):
    dic = {}
    for tan in tangerine:
        dic[tan] = 0
    for tan in tangerine:
        dic[tan] += 1
    dic_ = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    sum_ = 0
    i = 0
    while sum_ < k:
        sum_ += dic_[i][1]
        i += 1
    return i