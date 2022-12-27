def solution(priorities, location):
    answer = 0
    documents = list(range(1,len(priorities)+1))
    want = documents[location]
    while priorities:
        prior = priorities.pop(0)
        document = documents.pop(0)
        if priorities and prior >= max(priorities):
            answer += 1
            if document == want:
                return answer
        elif not priorities:
            answer += 1
            return answer
        elif prior < max(priorities):
            priorities.append(prior)
            documents.append(document)