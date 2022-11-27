from collections import Counter

def solution(X, Y):
    answer = ''
    A, B = Counter(X), Counter(Y)
    list_a, list_b = A.keys(), B.keys()
    for i in list_a:
        if i in list_b:
            answer += str(i)*min(A[i], B[i])
    if answer:
        answer = ''.join(sorted(answer, reverse=True))
        if answer[0] == '0':
            return '0'
        return answer
    else:
        return '-1'

X = "5525"
Y  ="1255"

a = solution(X, Y)
print(a)