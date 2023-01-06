def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        cash = []
        for j in range(len(arr1[0])):
            cash.append(arr1[i][j]+arr2[i][j])
        answer.append(cash)
    return answer