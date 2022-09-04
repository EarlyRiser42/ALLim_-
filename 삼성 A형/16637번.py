def calculate(num1, order, num2): # '+', '-', 'x'을 연산하는 함수
    if order == '+':
        return num1 + num2
    elif order == '-':
        return num1 - num2
    else:
        return num1 * num2


def move(idx, cnt, flag, orders):  # dfs
    global count
    if cnt == count: # 연산자 수 만큼 탐색을 완료했으면
        candidates.append(orders) # 남은 연산들이 담긴 orders는 candidates에 담는다.
        return
    if flag: # 이전에 괄호를 사용했으면 다음에는 무조건 사용X
        move(idx+2, cnt+1, False, orders) 
    else: # 이전에 괄호를 사용하지 않았으면 두 가지 경우가 존재한다.
        move(idx, cnt+1, True, orders[:idx-1] + [calculate(orders[idx-1], orders[idx], orders[idx+1])] + orders[idx+2:]) # 1. 괄호를 사용하는 경우 (해당 연산을 미리 계산한다.)
        move(idx+2, cnt+1, False, orders) # 2. 다음에도 사용하지 않는 경우


order = ['+', '-', '*']
N = int(input())
origin = input()
answer = -0xfffffff
orders = []
candidates = []

num = ''
for unit in origin: # 주어진 계산식(input)을 숫자, 연산자로 분리한다.
    if unit not in order:
        num += unit
    else:
        orders.append(int(num))
        orders.append(unit)
        num = ''
orders.append(int(num))

count = len(orders)//2
move(1, 0, False, orders)

for candidate in candidates:
    target = candidate[::-1]
    for i in range(len(candidate)//2):
        target.append(calculate(target.pop(), target.pop(), target.pop()))
    answer = max(answer, target[0])
print(answer)