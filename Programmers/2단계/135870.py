def solution(arrayA, arrayB):
    A, B = [], []
    cash = 0
    for j in range(1,int(arrayA[0]//2)+1):
        if arrayA[0] % j == 0:
            A.append(j)
    A.append(arrayA[0])
    for j in range(1,int(arrayB[0]//2)+1):
        if arrayB[0] % j == 0:
            B.append(j)
    B.append(arrayB[0])
    candidate = []
    for yaksu in A:
        stan = 0
        for i in arrayA[1:]:
            if i%yaksu != 0:
                stan = 1
                break
        if stan == 0:
            candidate.append(yaksu)
    cash2 = 0
    for can in candidate:
        stan = 0
        for i in arrayB:
            if i % can == 0:
                stan = 1
                break
        if stan == 0:
            cash = can
    candidate = []
    for yaksu in B:
        stan = 0
        for i in arrayB[1:]:
            if i%yaksu != 0:
                stan = 1
                break
        if stan == 0:
            candidate.append(yaksu)
    for can in candidate:
        stan = 0
        for i in arrayA:
            if i % can == 0:
                stan = 1
                break
        if stan == 0:
            cash2 = can
    answer = max(cash, cash2)
    return answer