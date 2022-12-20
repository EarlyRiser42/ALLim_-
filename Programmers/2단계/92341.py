import math


def solution(fees, records):
    answer = []
    dic = {}
    # 번호판, 시, 분 순으로 정렬
    records.sort(key=lambda x:(x[6:11], x[0:2], x[3:5]))
    # dictionary 초기화
    for record in records:
        dic[record[6:11]] = 0
    i = 0
    while i < len(records):
        # records 길이가 홀수일 경우 i와 i+1을 비교할 수 없고, i==len(records)-1이면 배열의 마지막 원소이므로 입차만 한 차
        if i == len(records)-1:
            time = (59 - int(records[i][3:5])) + (23 - int(records[i][0:2])) * 60
            if time <= fees[0]:
                dic[records[i][6:11]] += time
            else:
                dic[records[i][6:11]] += time
            break
        # 번호판 순으로 정렬했으므로 i와 i+1의 번호판이 같다면 각각 in, out이다.
        if records[i][6:11] == records[i+1][6:11]:
            time = (int(records[i+1][3:5])-int(records[i][3:5]))+(int(records[i+1][0:2])-int(records[i][0:2]))*60
            if time <= fees[0]:
                dic[records[i][6:11]] += time
            else:
                dic[records[i][6:11]] += time
            i += 2
        # i와 i+1의 번호판이 다르다면 i번째 차는 입차만 한 차이다. 따라서 23:59분에 출차한 것으로 계산한다.
        else:
            time = (59-int(records[i][3:5]))+(23-int(records[i][0:2]))*60
            if time <= fees[0]:
                dic[records[i][6:11]] += time
            else:
                dic[records[i][6:11]] += time
            i += 1

    for key in list(dic.keys()):
        if dic[key] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append((fees[1]+math.ceil((dic[key]-fees[0])/fees[2])*fees[3]))
    return answer
