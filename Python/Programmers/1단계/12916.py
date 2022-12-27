def solution(s):
    answer = True
    s = s.lower()
    p, y = 0, 0
    for word in s:
        if word == 'p':
            p += 1
        elif word == 'y':
            y += 1
        else:
            continue
    if p == y:
        return True
    else:
        return False