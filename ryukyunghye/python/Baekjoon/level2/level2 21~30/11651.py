# [11651] 좌표 정렬하기2
import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    data.append([b, a])
sorted_data = sorted(data)
for b, a in sorted_data:
    print(a, b)
