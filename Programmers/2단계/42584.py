def solution(prices):
    answer = []
    for i in range(len(prices)):
        price = prices[i]
        j = i+1
        while j < len(prices)-1 and price <= prices[j]:
            j+=1
        answer.append(j-i)
    answer[-1] = 0
    return answer