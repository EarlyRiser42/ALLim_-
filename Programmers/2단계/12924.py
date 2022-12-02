def solution(n):
    answer = 1
    j = 1
    while j < (n//2)+1:
        cash = 0
        for i in range(j,(n//2)+2):
            cash += i
            if cash == n:
                answer += 1
                break
            elif cash > n:
                break
        j += 1
    return answer


print(solution(10000))
