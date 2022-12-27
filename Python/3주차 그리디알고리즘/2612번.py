import sys

sensor_num = sys.stdin.readline()
center_num = sys.stdin.readline()

sensor_x = list(map(int, sys.stdin.readline().split()))
sensor_x.sort()
center_x = []
sensor_diff = []

print(sensor_x)
for x in range(int(sensor_num)-1):
    sensor_diff.append(sensor_x[x+1]-sensor_x[x])

print(f'  {sensor_diff}')
sensor_diff.sort()
sum = sum(sensor_diff[:int(sensor_num)-int(center_num)])
print(sum)
