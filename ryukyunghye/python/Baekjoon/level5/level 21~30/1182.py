# [1182] 부분수열의 합
from itertools import combinations, permutations

n, s = map(int, input().split())
numberList = list(map(int, input().split()))
result = 0

for i in range(1, n+1):
    for c in combinations(numberList, i):
        if sum(c) == s:
            result += 1

print(result)
