def solution(id_list, report, k):
    answer = [0] * len(id_list)
    idx_of = {}
    reporters = [set() for _ in range(len(id_list))]

    for name in range(len(id_list)):
        idx_of[id_list[name]] = name

    print(idx_of)

    for name in report:
        rpter, rpted = name.split()
        reporters[idx_of[rpted]].add(idx_of[rpter])

    print(reporters)

    for i in range(len(id_list)):
        if len(reporters[i]) >= k:
            for j in reporters[i]:
                answer[j] += 1

    return answer

a= solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print(a)
