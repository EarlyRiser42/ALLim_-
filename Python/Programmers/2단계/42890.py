from itertools import combinations


def solution(relation):
    answer = []
    for i in range(1, len(relation[0])+1):
        combi = list(combinations(list(range(0, len(relation[0]))), i))
        for com in combi:
            cash = set()
            for j in range(len(relation)):
                candidate = ''
                for k in com:
                    candidate += relation[j][k]
                cash.add(candidate)
            if len(relation) == len(cash):
                answer.append(com)
    result = [answer[0]]
    for ans in answer:
        dupli = False
        for rslt in result:
            a = len(set(ans)-set(rslt))
            b = len(ans) - len(rslt)
            if a == b:
                dupli = True
                break
        if not dupli:
            result.append(ans)
    return len(result)


print(solution([["100","ryan","music","2"],["100","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))