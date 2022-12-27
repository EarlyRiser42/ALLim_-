def solution(cacheSize, cities):
    answer = 0
    queue = []
    if cacheSize == 0:
        return 5*len(cities)
    for city in cities:
        city = city.lower()
        if len(queue) >= cacheSize:
            if city in queue:
                queue.pop(queue.index(city))
                queue.append(city)
                answer += 1
            else:
                if queue:
                    del queue[0]
                    queue.append(city)
                    answer += 5
                else:
                    queue.append(city)
                    answer += 5
        else:
            if city.lower() in queue:
                queue.append(city)
                answer += 1
            else:
                queue.append(city)
                answer += 5
    return answer