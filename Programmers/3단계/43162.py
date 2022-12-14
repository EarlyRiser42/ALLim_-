def dfs(node, graph, visited):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child, graph, visited)


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    # 인접 행렬 구현
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                if i not in graph[j]:
                    graph[j].append(i)
                if j not in graph[i]:
                    graph[i].append(j)
    # 방문 여부 배열
    visited = [False for __ in range(n)]
    for k in range(n):
        if not visited[k]:
            dfs(k, graph, visited)
            answer += 1
    return answer