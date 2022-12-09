def solution(array, commands):
    answer = []
    for command in commands:
        cash = array[command[0]-1:command[1]]
        cash.sort()
        answer.append(cash[command[2]-1])
    return answer
