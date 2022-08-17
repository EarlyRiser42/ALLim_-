import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort()

if N == 1:
    print(tree[0]-M)
    sys.exit(0)

cnt = 0
if M > tree[-1]:
    start, end = tree[-1], M
    left, right = 0, M - tree[-1]
else:
    start, end = M, tree[-1]
    left, right = 0, tree[-1] - M

i = (left+right)//2

while cnt != M:
    cnt = 0
    cut = pre[i]
    for tre in tree:
        if tre > cut:
            cnt += tre - cut
    if cnt > M:
        i = (right + i) // 2
    else:
        i = (left + i) // 2

print(cut)
