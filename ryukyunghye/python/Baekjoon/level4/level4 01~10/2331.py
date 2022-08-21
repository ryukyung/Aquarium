# [2331] 반복수열
a, p = map(int, input().split())
numberList = [a]

while True:
    newNumber = 0
    for i in str(numberList[-1]):
        newNumber += int(i) ** p
    if newNumber in numberList:
        break
    numberList.append(newNumber)

print(numberList.index(newNumber))
