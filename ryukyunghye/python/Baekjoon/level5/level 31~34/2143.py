# [2143] 두 배열의 합
from bisect import bisect_left, bisect_right
import sys

k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

aList = []
bList = []
result = 0

for i in range(n):
    total = 0
    for j in range(i, n):
        total += a[j]
        aList.append(total)

for i in range(m):
    total = 0
    for j in range(i, m):
        total += b[j]
        bList.append(total)
bList.sort()

for aList in aList:
    total = k - aList
    left = bisect_left(bList, total)
    right = bisect_right(bList, total)
    result += right-left
print(result)
