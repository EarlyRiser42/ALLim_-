import sys

T = int(sys.stdin.readline())
for _ in range(T):
    series = []
    M = int(sys.stdin.readline())
    if M > 10:
        a = M // 10
        for __ in range(a+1):
            series += list((map(int, sys.stdin.readline().split())))
    else:
        series = list(map(int, sys.stdin.readline().split()))

    print(M // 2 + 1)
    print(series[0], end=" ")
    if M != 1:
        cnt = 1
        for i in range(2, M, 2):
            print(sorted(series[:i + 1])[(i + 1) // 2], end=" ")
            cnt += 1
            if cnt == 10:
                print()
                cnt = 0
        else:
            print()
