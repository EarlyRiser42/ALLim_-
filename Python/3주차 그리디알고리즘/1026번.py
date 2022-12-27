import sys

number = sys.stdin.readline()

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)
output = 0
for x in range(int(number)):
    output += (A[x]*B[x])

print(output)
