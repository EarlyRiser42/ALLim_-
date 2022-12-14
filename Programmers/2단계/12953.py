def solution(arr):
    max_ = max(arr)
    i = 1
    while True:
        max_ *= i
        min_mul = 0
        for a in arr:
            if max_%a == 0:
                min_mul += 1
            else:
                break
        if min_mul == len(arr):
            return max_
        max_ = max(arr)
        i += 1