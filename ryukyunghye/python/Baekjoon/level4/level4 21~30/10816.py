# [10816] 숫자카드2
# 시간초과 해결X
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
n = int(input())
card = sorted(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start > end:
        return None
    middle = (start+end)//2

    if array[middle] == target:
        return array[start:end+1].count(target)
    elif array[middle] > target:
        return binary_search(array, target, start, middle-1)
    else:
        return binary_search(array, target, middle+1, end)


for i in range(len(compare)):
    result = binary_search(card, compare[i], 0, len(card)-1)
    if result is not None:
        print(result, end=' ')
    else:
        print(0, end=' ')

'''
bisect: 파이썬 내장 이진탐색 모듈 
bisect_left(literable, value): 왼쪽 인덱스 구하기
bisect_right(literable, value): 오른쪽 인덱스 구하기
'''
# from bisect import bisect_left, bisect_right
n = int(input())
card = sorted(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))


def count_by_range(array, leftValue, rightValue):
    rightIndex = bisect_right(array, rightValue)
    leftIndex = bisect_left(array, leftValue)
    return rightIndex - leftIndex


for i in range(len(compare)):
    print(count_by_range(card, compare[i], compare[i]), end=' ')
