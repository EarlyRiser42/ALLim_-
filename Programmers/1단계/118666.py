def solution(survey, choices):
    length = len(survey)
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # 삽입
    for i in range(length):
        if choices[i] < 4:
            if choices[i] == 1:
                score[survey[i][0]] += 3
            elif choices[i] == 3:
                score[survey[i][0]] += 1
            else:
                score[survey[i][0]] += choices[i]
        elif choices[i] > 4:
            score[survey[i][1]] += (choices[i]-4)
        else:
            continue
    answer = ''
    # MBTI 반환
    for mbti in [('R', 'T'), ('C','F'), ('J','M'), ('A','N')]:
        if score[mbti[1]] > score[mbti[0]]:
            answer += mbti[1]
        else:
            answer += mbti[0]
    return answer

survey = ["TR", "RT", "TR"]
choices = 	[7, 1, 3]

ans = solution(survey, choices)
print(ans)