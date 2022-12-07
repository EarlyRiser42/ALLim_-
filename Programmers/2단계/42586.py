import math

def solution(progresses, speeds):
    answer = []
    times = []
    for i in range(len(progresses)):
        left = math.ceil((100-progresses[i])/speeds[i])
        times.append(left)

    while times:
        cnt = 1
        time = times.pop(0)
        while times and times[0] <= time:
            del times[0]
            cnt += 1
        answer.append(cnt)
    return answer
