from itertools import permutations


def solution(k, dungeons):
    answer = -1
    permutation = list(permutations(list(range(len(dungeons))), len(dungeons)))
    for per in permutation:
        cash = k
        cnt = 0
        for p in per:
            if cash >= dungeons[p][0]:
                cash -= dungeons[p][1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
    return answer