import sys

def triangle_area(x, y, z):
    return abs((x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-x[1]*y[0]-y[1]*z[0]-z[1]*x[0]))/2


jum = []
inp = sys.stdin.readline()
for i in range(int(inp)):
    inpp = sys.stdin.readline()
    jum.append(list(map(int, inpp.split())))

while len(jum) > 2:
    x = 0
    print(triangle_area(jum[x], jum[x+1], jum[x+2]))
    jum.pop(int((x+1)))

