def solution(k, ranges):
    answer = []
    graph = [k]
    i = 1
    while k > 1:
        if k%2 == 0:
            k = k//2
            graph.append(k)
        else:
            k = (3*k)+1
            graph.append(k)
        i += 1
    for ran in ranges:
        start, end = ran[0], len(graph)+ran[1]-1
        if start > end:
            answer.append(-1.0)
        elif start == end:
            answer.append(0.0)
        else:
            cash = 0

            for i in range(start,end):
                cash += (graph[i]+graph[i+1])/2
            answer.append(float(cash))
    return answer