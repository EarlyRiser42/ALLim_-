from math import sqrt

def get_yaksu(number):
    ans = 0  # number는 무조건 약수
    cash = 0
    for i in range(1, int(sqrt(number))+1):
        if number%i == 0:
            ans += 1
    if int(sqrt(number))*int(sqrt(number)) == number:
        cash = -1
    ans *= 2
    return ans+ cash

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cash = get_yaksu(i)
        if cash%2 == 0:
            answer += i
        else:
            answer -= i
    return answer