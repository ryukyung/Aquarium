# [2751] 수 정렬하기2
import sys
n = int(input())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))
for i in sorted(data):
    sys.stdout.write(str(i)+'\n')
