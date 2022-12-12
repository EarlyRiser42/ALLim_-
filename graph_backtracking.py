def dfs(node, graph, cnt, n, costs):
    global min_
    if len(cnt) == n:
        cash = 0
        for i in range(n-1):
            for cost in costs:
                if cnt[i:i+2] == cost[:2] or cnt[i:i+2] == cost[:2][::-1]:
                    cash += cost[2]
        if cash < min_:
            min_ = cash
        return
    for child in graph[node]:
        if child not in cnt:
            cnt.append(child)
            dfs(child, graph, cnt, n, costs)
            cnt.pop()


def solution(n, costs):
    global min_
    graph = [[] for _ in range(n)]
    for cost in costs:
        graph[cost[0]].append(cost[1])
        graph[cost[1]].append(cost[0])
    min_ = float('inf')

    for i in range(n):
        cnt = [i]
        dfs(i, graph, cnt, n, costs)
    answer = min_
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
