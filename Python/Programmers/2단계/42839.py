from itertools import permutations


def solution(numbers):
    result = set()
    for i in range(1, len(list(numbers))+1):
        permu = list(permutations(list(numbers), i))
        for per in permu:
            p = int(''.join(per))
            if p == 1:
                continue
            cnt = 0
            for j in range(1, int(p**0.5)+1):
                if p%j == 0:
                    cnt += 1
            if cnt == 1:
                result.add(p)
    answer = len(result)
    return answer
