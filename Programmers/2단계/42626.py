import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 2:
            if len(scoville) == 2 and scoville[0] + scoville[1]*2 >= K:
                    return answer + 1
            else:
                return -1
        else:
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, s1+s2*2)
            answer += 1
    return answer
