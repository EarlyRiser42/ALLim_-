def solution(s):
    length = len(s)
    if length == 1:
        return 1
    ans_len = 10000
    for i in range(1, length):
        cnt = 1
        candidate = ''
        for j in range(0, length, i):
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt += 1
            else:
                if cnt == 1:
                    candidate += s[j:j+i]
                else:
                    candidate += str(cnt)+s[j:j+i]
                cnt = 1
            # print(f'구간1:({j},{j+i}) 구간2:({j+i},{j+2*i}), candidate: {candidate}')
        if j+i != length:
            candidate += s[j+i:length]
        #print(f'i: {i}, candidate: {candidate}')
        if len(candidate) < ans_len:
            ans_len = len(candidate)
    return ans_len

print(solution("aa"))