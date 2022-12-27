def solution(s):
    s = s[1:len(s)]
    answer = []
    dic = {}
    i = 0
    while i < len(s):
        if s[i] == '{':
            cash = []
            i += 1
            while s[i] != '}':
                if s[i] == ',':
                    i += 1
                num = s[i]
                i += 1
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                cash.append(int(num))
            dic[len(cash)] = cash
        else:
            i += 1

    for key in range(1,len(dic.keys())+1):
        for value in dic[key]:
            if value not in answer:
                answer.append(value)
    return answer