# [1934] 최소공배수
import math
testCase = int(input())
for i in range(0, testCase):
    number1, number2 = map(int, input().split())
    print(math.lcm(number1, number2))
