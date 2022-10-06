import sys
from itertools import combinations
from copy import deepcopy


def length(x,y,x2,y2):
    return abs(x-x2)+abs(y-y2)


N, M, D = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

candidates = list(combinations(range(M), 3))  # 0~M-1열중에 3개에 배치 되므로 [0:M]개중에 3개를 뽑는다
max_ = 0

for candidate in candidates:  # 조합으로 궁수 세명 경우의 수
    cnt = 0
    graph_for = deepcopy(graph)

    for row in range(N):  # N번 반복
        pre = [[], [], []]
        for three in range(3):  # 궁수 세명
            for d in range(D):  # 사정 거리가 D인 경우, N-1행부터 N-1-D행까지 닿으니깐 (직선 거리)
                for col in range(M):
                    if 0 <= N-1-d < N and graph_for[N-1-d][col] == 1:
                        pre[three].append((length(N-1-d, col, N, candidate[three]), N-1-d, col))

        for sam in range(3):  # 한번에 하나만 지울 수 있음
            pre[sam].sort(key=(lambda x: (x[0], x[2])))  # 거리 최소, 거리가 같으면 제일 작은 인덱스
            if pre[sam]:  # 빈 배열이 있을 수도 있어서
                r, c = pre[sam][0][1], pre[sam][0][2]
                if pre[sam][0][0] <= D and graph_for[r][c] == 1:
                    # 36줄에서 배열 값을 0으로 하므로 이미 공격한 곳을 다시 공격X(동시 공격 가능하나, 카운트는 하나만 늘려야 하기에)
                    cnt += 1
                    graph_for[r][c] = 0

        # 그래프 한칸 내리기
        for move in range(-1, -N, -1):
            graph_for[move] = graph_for[move - 1]
        graph_for[0] = [0 for __ in range(M)]

    max_ = max(cnt, max_)

print(max_)
