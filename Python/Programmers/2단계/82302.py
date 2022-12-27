from itertools import combinations


def solution(places):
    answer = []
    for place in places:
        student = []
        judge = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    student.append((i,j))
        combination = list(combinations(student, 2))
        for combi in combination:
            x_shape = abs(combi[0][0] - combi[1][0])
            y_shape = abs(combi[0][1] - combi[1][1])
            if x_shape + y_shape == 2:
                # 수직으로 배치 돼있음
                if x_shape == 0 and place[combi[0][0]][(combi[0][1]+combi[1][1])//2] != 'X':
                    judge = 1
                    answer.append(0)
                    break
                # 수평으로 배치 돼잇음
                elif y_shape == 0 and place[(combi[0][0]+combi[1][0])//2][combi[0][1]] != 'X':
                    judge = 1
                    answer.append(0)
                    break
                # 대각선으로
                elif x_shape == 1 and y_shape == 1:
                    list(combi).sort(key= lambda x:x[0])
                    if combi[0][1] > combi[1][1]:
                        if place[combi[0][0]+1][combi[0][1]] != 'X':
                            judge = 1
                            answer.append(0)
                            break
                        if place[combi[0][0]][combi[0][1] - 1] != 'X':
                            judge = 1
                            answer.append(0)
                            break
                    elif combi[1][1] > combi[0][1]:
                        if place[combi[0][0]][combi[0][1]+1] != 'X':
                            judge = 1
                            answer.append(0)
                            break
                        if place[combi[0][0]+1][combi[0][1]] != 'X':
                            judge = 1
                            answer.append(0)
                            break
            elif x_shape + y_shape < 2:
                judge = 1
                answer.append(0)
                break
        if judge == 0:
            answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))