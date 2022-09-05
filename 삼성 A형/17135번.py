import sys
from itertools import combinations
import heapq
from copy import deepcopy


def length(x,y,x2,y2):
    return abs(x-x2)+abs(y-y2)


N, M, D = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
candidates = list(combinations(range(N), 3))

max = 0

for candidate in candidates:  # 조합으로 궁수 세명 경우의 수
    cnt = 0
    duplication = set()
    graph_for = deepcopy(graph)
    for row in range(N-1, -1, -1):  # N-1행부터 시작, 0까지
        pre = [[], [], []]
        for three in range(3):  # 궁수 세명
            for d in range(D):  # 사정거리가 D인경우, N-1행부터 N-1-D행까지 닿으니깐 (직선거리)
                for col in range(M):  # 왼쪽부터 지우니깐 열은 0열부터 시작
                    if graph_for[row-d][col] == 1:
                        # 범위를 위한 조건 추가
                        heapq.heappush(pre[three], (length(row+d+1, col, N, candidate[three]), (row-d, col)))  # 거리가 최소인걸 쏘므로 우선순위큐 사용 + 거리가 같으면 왼쪽 인덱스
        for sam in range(3):  # 한번에 하나만 지울 수 있음
            if pre[sam] and pre[sam][0][0] <= D:
                print(pre[sam])
                r, c = pre[sam][0][1][0], pre[sam][0][1][1]
                duplication.add((r, c))
                graph_for[r][c] = 0
                print(candidate, duplication)
        cnt = len(duplication)
    if cnt > max:
        save = candidate
        max = cnt

print(max)
