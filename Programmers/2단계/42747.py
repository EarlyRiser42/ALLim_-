from bisect import bisect_left, bisect_right


def solution(citations):
    answer = 0
    citations.sort()
    for i in range(citations[-1]+1):
        left = bisect_left(citations, i)
        right = bisect_right(citations, i)
        if (right-left) >= 2:
            less = len(citations[:left+right-left])
            more = len(citations[left:])
        else:
            if citations[left] == i:
                less = len(citations[:left+1])
                more = len(citations[left:])
            else:
                less = len(citations[:left])
                more = len(citations[left:])
        if more >= i >= less and i >= answer:
            answer = i
    return answer