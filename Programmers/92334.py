def solution(id_list, report, k):
    count, ans, cash = {}, {}, set()
    for idd in id_list:
        count[idd] = 0
    for iddd in id_list:
        ans[iddd] = 0

    for singo in report:
        if singo not in cash:
            count[singo.split(' ')[1]] += 1
            cash.add(singo)

    susppend_users = []
    for key in id_list:
        if count[key] >= k:
            susppend_users.append(key)

    for users in susppend_users:
        for ca in cash:
            if ca.split(' ')[1] == users:
                ans[ca.split(' ')[0]] += 1
    answer = list(ans.values())
    return answer