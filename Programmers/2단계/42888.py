def solution(record):
    answer = []
    dic = {}
    for re in record:
        cash = re.split(' ')
        if cash[0] == 'Enter':
            dic[cash[1]] = cash[2]
        elif cash[0] == 'Change':
            dic[cash[1]] = cash[2]
        else:
            continue

    for re in record:
        cash = re.split(' ')
        if cash[0] == 'Enter':
            answer.append(dic[cash[1]] + '님이 들어왔습니다.')
        elif cash[0] == 'Leave':
            answer.append(dic[cash[1]] + '님이 나갔습니다.')
    return answer