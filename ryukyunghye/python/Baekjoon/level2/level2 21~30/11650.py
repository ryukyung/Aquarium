# [11650] 좌표 정렬하기
import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    data.append([a, b])
sorted_data = sorted(data)
for i in range(n):
    print(sorted_data[i][0], sorted_data[i][1])
