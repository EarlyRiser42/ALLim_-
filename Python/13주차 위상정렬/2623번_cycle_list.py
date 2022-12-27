import sys


def dfs(n):
    visited[n] = True
    for child in tree[n]:
        if not visited[child]:
            dfs(child)
        elif not finished[child]:  # 부모 노드가 finished[child] = True가 아니다 -> 자식 노드에서 다시 방문하였다 -> cycle 존재
            print(0)
            sys.exit(0)
    rslt.append(n+1)
    finished[n] = True  # 자식 노드부터 finished[n] = True



N, M = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N)]
visited = [False for __ in range(N)]
finished = [False for ___ in range(N)]
rslt = []

for _ in range(M):
    list_ = list(map(int, sys.stdin.readline().split()))
    for i in range(list_[0]-1):
        tree[list_[i+1]-1].append(list_[i+2]-1)

for j in range(N):
    if not visited[j]:
        dfs(j)

rslt.reverse()

for k in rslt:
    print(k)
