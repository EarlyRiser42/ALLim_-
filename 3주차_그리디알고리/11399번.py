import sys


def calculate_time_sum(lists):
    pre = 0
    for x in range(1, 1+len(lists)):
        pre += sum(lists[0:x])
    return pre


num = sys.stdin.readline()
ppl = list(map(int, sys.stdin.readline().split()))
ppl.sort()

print(calculate_time_sum(ppl))
