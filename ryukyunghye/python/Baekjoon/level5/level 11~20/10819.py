# [10819] 차이를 최대로
from itertools import permutations
n = int(input())
aList = list(map(int, input().split()))
result = 0

for p in permutations(aList):
    calculator = 0
    for i in range(n-1):
        calculator += abs(p[i]-p[i+1])
    result = max(result, calculator)

print(result)
