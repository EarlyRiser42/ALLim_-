import sys
from collections import deque

num = int(sys.stdin.readline())
docu = []
importance = []

for i in range(num*2):
    if i % 2 == 0:
        # 첫째줄 입력, 문서의 개수/ 궁금한 문서가 몇 번째에 있는지
        inputt = list(map(int, sys.stdin.readline().split()))
        importance.append(inputt)
    else:
        # 둘째줄 입력, 중요도
        inputt = list(map(int, sys.stdin.readline().split()))
        docu.append(inputt)

for x in range(num):
    # list(deque) 만들기
    lists_1 = list(range(1, importance[x][0]+1))
    rslt = deque(lists_1)
    document = deque(docu[x])
    # 궁금한 문서 숫자를 저장
    answer = rslt[importance[x][1]]
    cnt = 0

    while rslt:
        # 뒤에 중요도 가 높은게 '하나 라도' 있다면 맨 뒤로 넘기기
        standard = max(document)
        if int(document[0]) == standard:
            b = rslt.popleft()
            document.popleft()
            cnt += 1
            if b == answer:
                print(cnt)
                break
        else:
            # 아니 라면 출력 하기(cnt 로 출력 카운트, pop 으로 출력 했다 침)
            a = rslt.popleft()
            rslt.append(a)
            c = document.popleft()
            document.append(c)
