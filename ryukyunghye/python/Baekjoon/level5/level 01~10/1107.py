# [1107] 리모컨
import sys
input = sys.stdin.readline
targetNumber = int(input())
breakButtonCount = int(input())
breakButton = list(map(int, input().split()))

result = abs(100 - targetNumber)

for number in range(1000001):
    number = str(number)

    for j in range(len(number)):
        if int(number[j]) in breakButton:
            break
        elif j == len(number) - 1:
            result = min(result, abs(int(number) - targetNumber) + len(number))

print(result)
