from array import *
import math

x = int(input())
a = array('i')  # 잔돈
b = [25,10,5,1]  # 동전 가치
c = array('i')  # 코인 개수
for i in range(0,x):
    y = int(input())
    a.append(y)

for k in range(0,x):
    c.append(math.floor(a[k]/b[0]))
    c.append(math.floor((a[k]%b[0])/b[1]))
    c.append(math.floor(((a[k] % b[0])%b[1])/b[2]))
    c.append(math.floor((((a[k] % b[0])%b[1])%b[2])/b[3]))
    print(c[0+4*k],"",c[1+4*k],"",c[2+4*k],"",c[3+4*k])


