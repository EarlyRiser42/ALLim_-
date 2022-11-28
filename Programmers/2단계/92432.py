def dfs(n, i, candidate, arrow, ans):
    print(ans)
    if arrow == n:
        return ans
    if arrow + candidate[1][i] <= n:
        arrow += candidate[1][i]
        ans.append(candidate[1][i])
    if i+1 < 11:
        dfs(n, i+1, candidate, arrow, ans)
        ans.pop()


def solution(n, info):
    # 라이언이 점수를 획득하기 위해 과녁별로 맞춰야 하는 화살의 갯수, 점수 배열
    candidate = [list(range(10,-1,-1)) for __ in range(2)]
    for i in range(10):
        candidate[1][i] = info[i]+1
    print(candidate[1])
    max_score = 0
    answer = list(range(len(info)))
    for i in range(10):
        ans = []
        result = dfs(n, i, candidate, 0, ans)
        print(i, result)
        score = 0
        # 라이언의 점수 계산
        for k in range(10):
            if result[k] != 0:
                score += candidate[0][k]
        if score > max_score:
            max_score, answer = score, result
        # 라이언의 점수가 같으면 낮은 과녁을 많이 맞춘 것을 선택
        elif score == max_score:
            print(answer, result)
            for j in range(10,-1,-1):
                if result[j] > answer[j]:
                    answer = result
                    break
    # 어피치 점수 계산 (한번만 계산해도 됌)
    appeach_score = 0
    for k in range(10):
        if info[k] > answer[k]:
            appeach_score += candidate[0][k]
    if appeach_score > max_score:
        return [-1]
    return answer

print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))