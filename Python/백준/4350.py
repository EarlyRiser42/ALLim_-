import sys

arr = []
for i in range(10000):
  num = sys.stdin.readline()
  if num == '\n':
    break
  arr.append(int(num))

for num in arr:
  cnt = 1
  temp = 1
  while(True):
    if temp % num ==0:  # temp가 num의 배수인지 확인
      print(cnt)
      break
    cnt+=1
    temp = temp*10 + 1  # 10을 곱하고 1을 더해주어 모든 자리수가 1인 수 만들기