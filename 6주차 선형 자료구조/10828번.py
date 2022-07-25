import sys

num = int(sys.stdin.readline())
input =[]
stack = []

for x in range(num):
    input_list = sys.stdin.readline().replace('\n','')
    input.append(input_list)

for y in input:
    if y.split(' ')[0] == 'push':
        stack.append(y.split(' ')[1])
    if y == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
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

