from copy import deepcopy


def dfs(node, tickets, visited):
    global cash
    global answer
    # 여행 경로의 길이는 tickets 길이에 1을 더한 값
    if len(cash) == len(tickets)+1:
        # 이미 경로를 정했는데 새로운 경로가 있을 경우
        if len(answer) == len(cash):
            j = 0
            # 기존 경로와 새로운 경로 중 알파벳 순서가 앞서는 경로를 찾기 위해 같은 index에서 서로 다른 공항값을 비교
            while j < len(cash)-1 and answer[j] == cash[j]:
                j += 1
            first, second = answer[j], cash[j]
            if first > second:
                answer = deepcopy(cash)
        else:
            answer = deepcopy(cash)
        return

    for i in range(len(tickets)):
        if tickets[i][0] == node and not visited[i]:
            visited[i] = True
            cash.append(tickets[i][1])
            dfs(tickets[i][1], tickets, visited)
            # 백트래킹
            cash.pop()
            visited[i] = False
    return


def solution(tickets):
    global answer
    global cash
    cash = ['ICN']
    answer = []
    visited = [False for _ in range(len(tickets))]
    dfs(cash[-1], tickets, visited)
    return answer

