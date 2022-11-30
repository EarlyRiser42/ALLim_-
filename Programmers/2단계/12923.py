from bisect import bisect_left


def get_yaksu(num):
    # 1은 모든 수의 약수
    yaksu = [1]
    # 제곱근까지 약수를 구함 으로써 탐색 범위를 줄임
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            yaksu.append(i)
    return yaksu


def solution(begin, end):
    answer = [0 for _ in range(begin, end+1)]
    for i in range(0, len(answer)):
        # begin과 길의 시작이 서로 달라 둘을 더해서 구간을 맞춤
        division = i + begin
        yaksu = get_yaksu(division)
        # 번호가 n인 블록은 2n부터 설치함으로 약수가 end를 2로 나눈 것보다 클 수 없음
        bound = bisect_left(yaksu, int(end//2)+1)
        # 소수가 아닌 경우와 소수인 경우 나누기
        if 1 < len(yaksu) == bound:
            cash = division // yaksu[1]
            if cash > 10000000:
                # 약수가 10^7보다 크면 제곱근 전 까지의 약수들로 나눈 수 중 10^7보다 작으며 최대인 값 찾기
                k, cash = 0, 1
                while k < len(yaksu) and cash <= 10000000:
                    temp = division // yaksu[k]
                    if cash < temp <= 10000000:
                        cash = temp
                    k += 1
            answer[i] = cash
        else:
            answer[i] = yaksu[bound-1]
    # 구간 맞추는 용으로 넣어둠
    if begin == 1:
        answer[0] = 0
    return answer
