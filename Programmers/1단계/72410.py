def solution(new_id):
    char = '~!@#$%^&*()=+[{]}:?,<>/'
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    cash = []
    for i in range(len(new_id)):
        if new_id[i] in char:
            continue
        else:
            cash.append(new_id[i])
    # 3단계, 4단계
    cash2 = [cash[0]]
    for i in range(1, len(cash)):
        if not cash2 and cash[i] == '.':
            continue
        elif cash2[-1] == '.' and cash[i] == '.':
            continue
        else:
            cash2.append(cash[i])
    if cash2[-1] == '.':
        del cash2[-1]
    if len(cash2) > 0 and cash2[0] == '.':
        del cash2[0]
    # 5단계
    if not cash2:
        cash2.append('a')
    # 6단계
    if len(cash2) > 15:
        cash2 = cash2[:15]
        if cash2[-1] == '.':
            cash2 = cash2[:14]
    # 7단계
    if len(cash2) <= 2:
        add = cash2[-1]
        while len(cash2) < 3:
            cash2.append(add)

    for element in cash2:
        answer += element
    return answer
