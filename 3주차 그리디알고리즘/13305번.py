#################### 내 풀이 17점
import sys

num = sys.stdin.readline()

distance = list(map(int, sys.stdin.readline().split()))

price = list(map(int, sys.stdin.readline().split()[:int(num)-1]))

total_price = distance[0]*price[0]

del distance[0]

cheapest = min(price[:len(price)-1])

x = 1
while x <= len(distance):
    if price[x] == cheapest:
        total_price += sum(distance)*price[x]
        break
    if price[x] < price[x+1]:
        total_price += (distance[x]+distance[x+1])*price[x]
        x += 2
    else:
        total_price += price[x]*distance[x]
        x += 1
print(total_price)
################################## 남 풀이 100 점
N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]
sum = 0
for i in range(N - 1):
    if minVal > cities[i]:
        minVal = cities[i]
    sum += (minVal * roads[i])

print(sum)