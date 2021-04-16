x = int(input())

ans = []
div = []
dap = []

div.append(x)

for i in range(x):
    y = divmod(div[i], 2)
    div.append(y[0])
    ans.append(y[1])
    if y[0] == 0:
        break

for i in range(len(ans)):
    dap.append(ans[len(ans)-i-1])

for i in range(len(dap)):
    print(dap[i], end='')
