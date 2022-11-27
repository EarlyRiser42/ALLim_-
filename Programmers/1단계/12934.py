def solution(n):
    if n == 1:
        return 4
    for i in range(n):
        if i*i == n:
            return (i+1)*(i+1)
        elif i*i > n:
            return -1
    return -1

a = solution(1)
print(a)