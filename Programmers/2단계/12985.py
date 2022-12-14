def solution(n,a,b):
    answer = 1
    if a > b:
        a,b = b, a
    while a > 1:
        if a%2 == 1 and abs(b-a)==1:
            break
        else:
            a = round(a/2)
            b = round(b/2)
            answer += 1
    return answer