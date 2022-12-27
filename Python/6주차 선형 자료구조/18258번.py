from collections import deque, defaultdict
import sys

num = int(sys.stdin.readline())
input = []
stack = deque()
for x in range(num):
    input_list = sys.stdin.readline().replace('\n','')
    input.append(input_list)

for y in input:
    if y.split(' ')[0] == 'push':
        stack.appendleft(int(y.split(' ')[1]))
    if y == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    if y == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    if y == 'size':
        print(len(stack))
    if y == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if y == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
