def solution(x, n):
    answer = []
    if x > 0:
        for i in range(x,x*n+1,x):
            answer.append(i)
        return answer
    elif x == 0:
        return [0 for _ in range(n)]
    else:
        for i in range(x,x*n-1,x):
            answer.append(i)
        return answer