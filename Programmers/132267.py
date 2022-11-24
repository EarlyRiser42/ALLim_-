import sys
sys.setrecursionlimit(10000)

def get_coke(ans, a,b,n):
    cash = n//a
    cash *= b
    ans += cash
    cash += (n%a)
    if cash < a:
        return ans
    else:
        return get_coke(ans,a,b,cash)


def solution(a, b, n):
    answer = get_coke(0,a,b,n)
    return answer
