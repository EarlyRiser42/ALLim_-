N = list(map(int, input()))

divide = len(N)//2
left, right = sum(N[0:divide]), sum(N[divide:len(N)])
if left == right:
    print('LUCKY')
else:
    print('READY')