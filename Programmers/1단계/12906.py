def solution(arr):
    answer = [arr[0]]
    for ar in arr[1:]:
        if ar != answer[-1]:
            answer.append(ar)
    return answer