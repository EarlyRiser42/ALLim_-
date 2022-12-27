def solution(answers):
    submit = [[1,2,3,4,5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    for i, sub in enumerate(submit):
        multiple = (len(answers)//len(sub))+1
        cash = sub*multiple
        cnt = 0
        for j in range(len(answers)):
            if cash[j] == answers[j]:
                cnt += 1
        answer.append((i+1,cnt))
    answer.sort(key=lambda x:x[1], reverse=True)
    result = [answer[0][0]]
    k = 1
    while k < 3 and answer[k][1] == answer[k-1][1]:
        result.append(answer[k][0])
        k += 1
    return result