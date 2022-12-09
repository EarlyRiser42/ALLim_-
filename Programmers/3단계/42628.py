import heapq


def solution(operations):
    heap = []
    for operation in operations:
        if operation[:1] == 'I':
            heapq.heappush(heap, int(operation[2:]))
        else:
            if heap:
                if operation[2] == '-':
                    del heap[0]
                else:
                    max_ = float('-inf')
                    for i in range(len(heap)):
                        if heap[i] >= max_:
                            max_ = heap[i]
                            j = i
                    del heap[j]
            else:
                continue
    if heap:
        return [max(heap), heap[0]]
    else:
        return [0,0]
