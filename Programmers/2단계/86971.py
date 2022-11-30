def dfs(parent, array, visit):
    global i
    i += 1
    visit[parent] = True
    for child in array[parent]:
        if not visit[child]:
            dfs(child, array, visit)
    return


def solution(n, wires):
    top = [[] for _ in range(n+1)]
    visited = [False for __ in range(n+1)]
    answer = 0
    for wire in wires:
        top[wire[0]].append(wire[1])
        top[wire[1]].append(wire[0])
    global i
    print(top)
    i = 0
    for j in range(1, n+1):
        top_cash = top.copy()
        child = top_cash[j]
        for ch in child:
            del top_cash[ch][top_cash[ch].index(j)]
        top_cash[j] = []
    dfs(1, top, visited)
    print(i)
    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	))