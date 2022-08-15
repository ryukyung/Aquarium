# [1158] 요세푸스 문제
n, k = map(int, input().split())
result = []
numberList = [i for i in range(1, n+1)]
number = 0
for i in range(n):
    number += (k-1)
    if number >= len(numberList):
        number %= len(numberList)
    result.append(str(numberList[number]))
    numberList.pop(number)
print("<", ', '.join(result), ">", sep="")
