import sys
from itertools import combinations

input = []

for i in range(0,9):
    input_prev = sys.stdin.readline()
    input.append(input_prev.replace('\n',''))

result = list(combinations(input, 7))

for x in range(0, len(result)):
    result[x] = list(map(int, result[x]))
    sums = sum(result[x])
    if sums == 100:
        for y in range(len(result[x])):
            print(result[x][y])
