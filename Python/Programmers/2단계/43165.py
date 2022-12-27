from itertools import combinations


def solution(numbers, target):
    answer = 0
    sum_ = sum(numbers)
    for i in range(1, len(numbers)+1):
        combination = list(combinations(list(range(len(numbers))), i))
        for combi in combination:
            cash = 0
            for c in combi:
                cash += numbers[c]
            if sum_ - cash*2 == target:
                answer += 1
    return answer

