def solution(babbling):
    can = [	['a', 'y', 'a'], ['y', 'e'], ['w', 'o', 'o'], ['m', 'a']]
    answer = 0
    for say in babbling:
        cash = []
        first= ''
        for i in range(len(say)):
            cash.append(say[i])
            if len(cash) > 1 and cash[-2:] in can:
                if cash[-2:] == first:
                    break
                first = cash[-2:]
                cash.pop()
                cash.pop()
                if cash:
                    break
            elif len(cash) > 2 and cash[-3:] in can:
                if cash[-3:] == first:
                    break
                first = cash[-3:]
                cash.pop()
                cash.pop()
                cash.pop()
                if cash:
                    break
        print(cash)
        if not cash:
            answer += 1
    return answer
