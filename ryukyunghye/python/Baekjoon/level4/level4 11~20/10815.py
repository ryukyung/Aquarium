# [10815] 숫자 카드
countNumber = int(input())
numberList = sorted(map(int, input().split()))
checkNumber = int(input())
checkList = list(map(int, input().split()))
result = []


def binary_search(i, numberList, start, end):
    middle = (start+end) // 2
    if start > end:
        result.append(0)
    elif i == numberList[middle]:
        result.append(1)
    elif i > numberList[middle]:
        binary_search(i, numberList, middle+1, end)
    else:
        binary_search(i, numberList, start, middle-1)


for i in checkList:
    start = 0
    end = len(numberList)-1
    binary_search(i, numberList, start, end)

print(*result)
