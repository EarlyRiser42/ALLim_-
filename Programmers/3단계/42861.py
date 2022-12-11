global costs


def dfs(node, visited):
    if len(cnt) == 4:
        print(cnt)
        return
    print(cnt)
    cnt.append(node)
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child, visited)
            cnt.pop()
            visited[node] = False


def solution(n, costs):
    global graph
    global cnt
    answer = 0
    cnt = []
    graph = [[] for _ in range(n)]
    for cost in costs:
        graph[cost[0]].append(cost[1])
        graph[cost[1]].append(cost[0])
    print(graph)
    visited = [False for _ in range(n)]
    dfs(0, visited)
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))