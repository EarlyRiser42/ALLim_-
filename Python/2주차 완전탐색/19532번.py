import sys

inpu = sys.stdin.readline()
input = list(map(int, inpu.split()))

for x in range(-999, 1000):
    for y in range(-999,1000):
        if input[0]*x + input[1]*y == input[2] and input[3]*x + input[4]*y == input[5]:
            print(f'{x} {y}')
            sys.exit(0)
