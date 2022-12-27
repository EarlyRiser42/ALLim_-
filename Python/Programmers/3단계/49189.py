from collections import deque


def bfs(graph, visited):
    global result
    # 인접 행렬은 부모 인덱스에 자식을, 자식 인덱스에 부모를 넣으므로 미리 visited[1]을 True로 해놔야 재방문하지 않는다.
    visited[1] = True
    # 노드의 번호와 간선 갯수를 deque에 넣음 ex: 노드의 번호 1의 간선 갯수는 0
    queue = deque([(1,0)])
    while queue:
        cash = queue.popleft()
        node, vertex = cash[0], cash[1]
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append((child, vertex+1))
                # 이전 노드의 간선 갯수에 1을 더하여 다음 노드의 간선 갯수를 셈
                result.append((child, vertex+1))


def solution(n, edge):
    global result
    result = []
    graph = [[] for _ in range(n+1)]
    visited = [False for __ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    bfs(graph, visited)
    answer = 1
    result.sort(key=lambda x:x[1], reverse=True)
    i = 0
    while i < len(result)-1 and result[i][1] == result[i+1][1]:
        answer += 1
        i += 1
    return answer