from copy import deepcopy

def dfs(node, array, visit):
    global num
    num += 1
    visit[node] = True
    for child in array[node]:
        if not visit[child]:
            dfs(child, array, visit)
    return


def solution(n, wires):
    global num
    answer = 100
    for i in range(len(wires)):
        wire = deepcopy(wires)
        a, b = wire[i][0], wire[i][1]
        del wire[i]
        top = [[] for _ in range(n+1)]
        for wir in wire:
            top[wir[0]].append(wir[1])
            top[wir[1]].append(wir[0])
        visited = [False for __ in range(n+1)]
        num = 0
        dfs(a, top, visited)
        first = num
        visited = [False for __ in range(n + 1)]
        num = 0
        dfs(b, top, visited)
        second = num
        if abs(first-second) < answer:
            answer = abs(first-second)
    return answer
