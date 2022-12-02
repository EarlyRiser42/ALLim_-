def get_yaksu(n):
    yaksu = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            yaksu.append(i)
    return yaksu


def solution(brown, yellow):
    total = brown + yellow
    yaksu = get_yaksu(total)
    w, h = total // yaksu[-1], yaksu[-1]
    answer = [w, h]
    return answer