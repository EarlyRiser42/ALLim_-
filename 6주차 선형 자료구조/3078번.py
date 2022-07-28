import sys

N, K = map(int, sys.stdin.readline().split())

name = []
cnt, combi = 0, 0

for i in range(N):
    name.append(sys.stdin.readline().rstrip())

for x in range(N):
    combi, standard = name.index(name[x]), name.index(name[x])
    print(name[x], x, combi)
    while combi < standard+2 and x+combi < N-1:
        combi += 1
        print(x+combi)
        if len(name[x]) == len(name[x+combi]):
            cnt += 1
            print(f'combi: {combi}, cnt:{cnt}, N:{N}')

print(cnt)
