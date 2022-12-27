def sosu(n):
    # 제곱근까지 약수가 없다면 소수, 하나라도 있다면 ~소수
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def convert(n, k):
    result = ''
    while n > k:
        # n의 몫이 k보다 작을때 까지 나누고, 나머지를 합치면 변환된 수
        a, b = divmod(n,k)
        result += str(b)
        n = a
    result += str(n)
    return result[::-1]


def solution(n, k):
    answer = 0
    result = convert(n,k)
    i = 0
    while i < len(result):
        cash = ''
        j = i
        while j < len(result) and result[j] != '0':
            cash += result[j]
            j += 1
        i = j
        i += 1
        if cash:
            if cash == '1':
                continue
            elif cash == '2':
                answer += 1
            else:
                if sosu(int(cash)):
                    answer += 1
    return answer