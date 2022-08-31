# [1208] 부분수열의 합2
import sys
from itertools import combinations
from bisect import bisect_left, bisect_right


def Number(list, find):
    return bisect_right(list, find) - bisect_left(list, find)


def Sum(list, totalList):
    for i in range(1, len(list)+1):
        for j in combinations(list, i):
            totalList.append(sum(j))
    totalList.sort()


n, s = map(int, input().split())
list = list(map(int, input().split()))

left, right = list[:n//2], list[n//2:]
leftTotal, rightTotal = [], []

Sum(left, leftTotal)
Sum(right, rightTotal)
result = 0
for i in leftTotal:
    find = s - i
    result += Number(rightTotal, find)

result += Number(leftTotal, s)
result += Number(rightTotal, s)
print(result)
