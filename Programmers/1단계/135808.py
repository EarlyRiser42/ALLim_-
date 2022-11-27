def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    iter = len(score)//m
    j = 0
    for i in range(iter):
        cash = score[j:m+j]
        min_ = cash[-1]
        answer += min_*m
        j += m
    return answer