def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve:
        for j in range(len(lost)):
            if lost and abs(lost[j] - i) == 1:
                del lost[j]
                break
            elif lost and abs(lost[j] - i) == 0:
                del lost[j]
                break 
    answer = n - len(lost)
    return answer