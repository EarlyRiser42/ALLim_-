def solution(s):
    cash = s.split()
    max_ = float('-inf')
    min_ = float('inf')
    for i in range(len(cash)):
        dummy = int(cash[i])
        if len(cash[i]) == 2:
            dummy = -1*int(cash[i][1])
        max_ = max(dummy, max_)
        min_ = min(dummy, min_)
    answer = str(min_)+' '+str(max_)
    return answer

a = solution("-1 -2 -3 -4")
print(a)
b = solution("1 2 3 4")
print(b)