import sys
from collections import Counter

num = int(sys.stdin.readline())
k= 9
alaphabet_num = []
alaphabet = []
z_where = []
for i in range(num):
    input = sys.stdin.readline().replace('\n','')
    alaphabet.append(input)
    alaphabet_num.append(len(input))

alaphabet.sort(reverse=True, key=lambda x: len(x))
alaphabet_num.sort(reverse=True)
alaphabet.append(alaphabet[len(alaphabet)-1])
alaphabet_num.append(alaphabet_num[len(alaphabet_num)-1])
cnt = Counter(alaphabet[0])

for x in range(1, num):
    cnt.update(alaphabet[x])

for y in range(num):
    z = 0
    while alaphabet_num[y] > alaphabet_num[y+1]:
        replacement = alaphabet[y].replace(alaphabet[y][z:z+1], str(k))
        alaphabet[y] = replacement

        alaphabet_num[y] -= 1
        k -= 1
        z += 1
    z_where.append(z)

for f in range(num):
    for name in z_where:
        standard = z_where[f]
        if cnt.get(alaphabet[f][standard:standard+1]) > cnt.get(alaphabet[f+1][standard:standard+1]):
            replacement = alaphabet[f].replace(alaphabet[f][standard:standard+1], str(k))
            replacement_2 = alaphabet[f+1].replace(alaphabet[f+1][standard:standard+1], str(k-1))
            alaphabet[f] = replacement
            alaphabet[f+1] = replacement_2
        else:
            replacement = alaphabet[f].replace(alaphabet[f][standard:standard+1], str(k-1))
            replacement_2 = alaphabet[f + 1].replace(alaphabet[f + 1][standard:standard+1], str(k))
            alaphabet[f] = replacement
            alaphabet[f + 1] = replacement_2
        print(alaphabet)
        k -= 1
print(alaphabet)
