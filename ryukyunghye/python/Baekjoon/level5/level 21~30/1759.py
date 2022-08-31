# [1759] 암호 만들기
from itertools import combinations
l, c = map(int, input().split())
alphaC = sorted(input().split())
combinationWord = combinations(alphaC, l)

for i in combinationWord:
    count = 0
    for j in i:
        if j in 'aeiou':
            count += 1
    if count >= 1 and (l - count) >= 2:
        print(''.join(i))
