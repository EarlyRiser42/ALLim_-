def solution(cards):
    answer = 0
    for i in range(len(cards)):
        visit = [False for _ in range(len(cards))]
        j = i
        cnt = 0
        while visit[j] == False:
            visit[j] = True
            j = cards[j]-1
            cnt += 1
        indexs = []
        for _ in range(len(visit)):
            if visit[_] == False:
                indexs.append(_)
        for index in indexs:
            j = index
            count = 0
            for _ in indexs:
                visit[_] = False
            while visit[j] == False:
                visit[j] = True
                j = cards[j]-1
                count += 1
            if count*cnt > answer:
                answer = count*cnt
    return answer