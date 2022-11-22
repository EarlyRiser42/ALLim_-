def solution(food):
    answer = ''
    cash = ''
    for i in range(1, len(food)):
        if food[i]%2 == 0:
            cash += str(i)*(food[i]//2)
        else:
            food[i] -= 1
            cash += str(i)*(food[i]//2)
    answer = cash+'0'+cash[::-1]
    return answer