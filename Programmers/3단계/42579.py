from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    sum = {}
    for genre in genres:
        sum[genre] = 0
    for i in range(len(plays)):
        sum[genres[i]] += plays[i]
    test = sorted(list(sum.items()), key=lambda x:x[1], reverse=True)

    for i in range(len(plays)):
        plays[i] = (i, plays[i])

    for i in range(len(genres)):
        dic[genres[i]].append(plays[i])

    for key in list(dic.keys()):
        dic[key].sort(key=lambda x:(x[1]), reverse=True)

    for key in test:
        if len(dic[key[0]]) > 1:
            for j in range(2):
                answer.append(dic[key[0]][j][0])
        else:
            answer.append(dic[key[0]][0][0])
    return answer