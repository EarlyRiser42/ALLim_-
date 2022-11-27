def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    i = 0
    if len(reserve) >= len(lost):
        while i < len(reserve):
            if reserve[i] in lost:
                del lost[lost.index(reserve[i])]
                del reserve[i]
                i = 0
            else:
                i += 1
    else:
        while i < len(lost):
            if lost[i] in reserve:
                del reserve[reserve.index(lost[i])]
                del lost[i]
                i = 0
            i += 1
    for i in reserve:
        j = 0
        while j < len(lost):
            if lost and abs(lost[j] - i) == 1:
                del lost[j]
                break
            elif lost and abs(lost[j] - i) == 0:
                del lost[j]
                break
            j += 1
    answer = n - len(lost)
    return answer
