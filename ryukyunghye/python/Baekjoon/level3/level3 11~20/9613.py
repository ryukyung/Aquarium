# [9613] GCD 합
import math
testCase = int(input())
for i in range(testCase):
    numberList = list(map(int, input().split()))
    result = 0
    for j in range(1, len(numberList)):
        for k in range(j+1, len(numberList)):
            result += math.gcd(numberList[j], numberList[k])
    print(result)
