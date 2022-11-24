def solution(dartResult):
    answer = []
    i = 0
    while i < len(dartResult):
        if dartResult[i] == '*':
            k = 0
            if answer:
                for j in range(len(answer)):
                    if k == 2:
                        break
                    answer[-1-j] = answer[-1-j]*2
                    k += 1
            i += 1
        elif dartResult[i] == '#':
            if answer:
                answer[-1] = answer[-1]*-1
            i += 1
        else:
            if dartResult[i+1] == 'S':
                answer.append(int(dartResult[i]))
                i += 2
            elif dartResult[i+1] == 'D':
                answer.append(int(dartResult[i])**2)
                i += 2
            elif dartResult[i+1] == 'T':
                answer.append(int(dartResult[i])**3)
                i += 2
            else:
                if dartResult[i + 2] == 'S':
                    answer.append(10)
                if dartResult[i + 2] == 'D':
                    answer.append(10 ** 2)
                if dartResult[i + 2] == 'T':
                    answer.append(10 ** 3)
                i += 3

    answer = sum(answer)
    return answer

print(solution('1D2S#10S'))