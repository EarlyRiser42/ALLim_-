def solution(s):
    answer = []
    for i in range(len(s)):
        print(s[i], s[:i])
        if s[i] in s[:i]:
            for j in range(1,i+1):
                if s[i-j] == s[i]:
                    answer.append(j)
                    break
        else:
            answer.append(-1)
    return answer
