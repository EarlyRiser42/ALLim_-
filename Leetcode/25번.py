head_ = input()
k = int(input())
head = head_[1:len(head_)-1].split(',')

repeat = (k+1)//2
diff = k-1

for i in range(0, len(head), k):
    diff = k-1
    if k % 2 == 0:
        for j in range(repeat):
            if 0 < i+diff < len(head):
                head[i+diff+j], head[i+j] = head[i+j], head[i+diff+j]
                diff -= 2
    else:
        for j in range(repeat):
            if 0 < i+diff < len(head):
                head[i+diff+j], head[i+j] = head[i+j], head[i+diff+j]
                diff -= 2

