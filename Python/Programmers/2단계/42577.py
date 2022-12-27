def solution(phone_book):
    s = {}
    min_ = float('inf')
    for phone in phone_book:
        if len(phone) < min_:
            min_ = len(phone)

    for p in phone_book:
        for i in range(min_, len(p)):
            s[p[:i]] = 1

    for p in phone_book:
        if p in s.keys():
            return False
    return True
