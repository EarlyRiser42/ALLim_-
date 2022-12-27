from string import ascii_uppercase


def solution(msg):
    answer = []
    dic = {}
    # dictionary 생성, 나중에 dictionary에 새로운 변수들을 저장하기 위해서 마지막 인덱스를 변수에 저장.
    last_i = 0
    for i, alphabet in enumerate(list(ascii_uppercase)):
        dic[alphabet] = i + 1
        last_i = i + 1
    # 인덱스가 불규칙하게 바뀌므로 while문 사용
    m = 0
    while m < len(msg):
        keys = list(dic.keys())
        cash = msg[m]
        index = m + 1
        while index < len(msg):
            # 시작문자열 + 다음문자열이 dictionary의 key들에 없을때까지 문자열 더함
            if cash + msg[index] in keys:
                cash += msg[index]
                index += 1
            else:
                break
        answer.append(dic[cash])
        # 22줄에서 index에 1을 더하기에 index가 문자열의 마지막 인덱스보다 커지는 것 방지
        if index < len(msg):
            dic[cash + msg[index]] = last_i + 1
            last_i += 1
        m = index
    return answer
