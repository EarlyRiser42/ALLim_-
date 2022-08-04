import sys


def find_parent(k):
    for i in tree[k]:
        if par[i] == 0:
            par[i] = par[k]+1
            find_parent(i)


n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]
par = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

find_parent(a)

print(tree[1:])
if par[b] > 0:
    print(par[b])
else:
    print('-1')
