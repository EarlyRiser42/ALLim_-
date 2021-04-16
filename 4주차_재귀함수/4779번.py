import math

def diva(x,y):
    if y-x == 0:
        c[0]='-'
        return 1
    n = round(math.log(y+1-x, 3))
    a = math.floor(((x+y) / 2) - (((3 ** (n - 1)) - 1) / 2))
    b = math.floor(((x+y) / 2) + (((3 ** (n - 1)) - 1) / 2))
    for i in range(a, b+1):
        c[i] = ' '
    if n <= 1:
        return 1
    else:
        return diva(x,a-1), diva(b+1,y)


babo = []
while True:
    try:
        line = input()
        if line:
            babo.append(line)
        else:
            break
    except:
        break

for i in range(len(babo)):
    c = ["-"]*(3**int(babo[i]))
    x = 0
    y = (3**int(babo[i]))-1
    diva(x, y)
    for m in range(len(c)):
        print(c[m], end='')
    if i == (len(babo)-1):
        break
    print(end='\n')
