def solution(info, query):
    answer = [0 for _ in range(len(query))]
    info.sort(key=lambda x:int(x.split()[-1]), reverse=True)
    information = {}
    for i in range(len(info)):
        key_value = info[i].split()
        information[str(key_value[:-1])] = int(key_value[-1])
    print(information)
    for j in range(len(query)):
        que = query[j].split()
        for ins in list(information.keys()):
            cash = 0
            print(ins, information[ins])
            if information[ins] >= int(que[-1]):
                for i in range(0, 7, 2):
                    if que[i] == '-':
                        continue
                    if que[i] not in ins:
                        cash = 1
                        break
                if cash == 0:
                    answer[j] += 1
            else:
                break
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))