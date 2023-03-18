n = int(input())
m = int(input())
nums = list(map(int, input().split())).sort()

cnt = 0
start = 0
end = n-1

while start<end:
    if nums[start] + nums[end] == m:
        cnt += 1
        start += 1
        end -= 1
    elif nums[start] + nums[end] < m:
        start += 1
    else:
        end -= 1

print(cnt)