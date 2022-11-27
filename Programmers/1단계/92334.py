def solution(id_list, report, k):
    answer = [0] * len(id_list)
    idx_of = {}
    reporters = [set() for _ in range(len(id_list))]

    # name에 숫자를 mapping함으로써 dictionary(14줄), set 접근을 원활하게 함
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
