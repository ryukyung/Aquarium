# [2805] 나무 자르기
# python - 시간초과,  pypy - 성공
import sys
input = sys.stdin.readline
countTree, lengthTree = map(int, input().split())
treeList = list(map(int, input().split()))
start, end = 1, max(treeList)

while start <= end:
    middle = (start+end)//2
    treeTotal = 0
    for i in treeList:
        if i >= middle:
            treeTotal += i - middle
    if treeTotal >= lengthTree:
        start = middle + 1
    else:
        end = middle - 1
print(end)
