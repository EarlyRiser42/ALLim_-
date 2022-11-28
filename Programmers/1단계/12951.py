def solution(s):
    print(f'len: {len(s)}')
    answer = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
            i += 1
            while s[i].isalpha() or s[i].isdigit():
                answer += s[i]
                i += 1
        elif s[i].isalpha():
            answer += s[i].upper()
            i += 1
            while s[i].isalpha() or s[i].isdigit():
                answer += s[i]
                i += 1
                print(answer, i)
        else:
            answer += s[i]
            i += 1
    return answer.rstrip()

a = solution("i    love you")
print(a)
