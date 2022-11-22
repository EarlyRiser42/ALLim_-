def solution(s):
    num_to_eng = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
                 'five':5, 'six':6, 'seven':7, 'eight':8,'nine':9}
    answer = ''
    j, i = 0, 0
    while j < len(s):
        print(answer)
        try:
            int(s[i])
            answer += s[i]
            j += 1
            i += 1
        except:
            cash = ''
            while cash not in list(num_to_eng.keys()):
                cash += s[i]
                i += 1
            answer += str(num_to_eng[cash])
            j += len(cash)
    return answer
