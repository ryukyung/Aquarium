# [1644] 소수의 연속합
# import math

n = int(input())

numbersList = [False, False] + [True] * (n-1)
primeNumber = []

for i in range(2, n+1):
    if numbersList[i]:
        primeNumber.append(i)
        for j in range(2*i, n+1, i):
            numbersList[j] = False

result = 0
startPoint = 0
endPoint = 0
while endPoint <= len(primeNumber):
    temp_sum = sum(primeNumber[startPoint:endPoint])
    if temp_sum == n:
        result += 1
        endPoint += 1
    elif temp_sum < n:
        endPoint += 1
    else:
        startPoint += 1

print(result)
