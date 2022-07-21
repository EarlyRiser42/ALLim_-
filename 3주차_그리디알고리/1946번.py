import sys

testcase = int(sys.stdin.readline())
grade = []
num_list = []
for i in range(testcase):
    num = int(sys.stdin.readline())
    num_list.append(num)
    for j in range(num):
        grade.append(list(map(int, sys.stdin.readline().split())))
print(grade)
for x in range(testcase):
    for y in range(num_list[x]):
        if
