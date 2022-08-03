# [11728] 배열 합치기
import sys
a, b = map(int, sys.stdin.readline().split())
aList = list(map(int, sys.stdin.readline().split()))
bList = list(map(int, sys.stdin.readline().split()))
resultList = sorted(aList+bList)
print(*resultList)
