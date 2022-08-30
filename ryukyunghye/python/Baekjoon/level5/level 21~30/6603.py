# [6603] 로또
from itertools import combinations

while True:
    numberList = list(map(int, input().split()))
    if numberList[0] == 0:
        break
    for i in combinations(numberList[1:], 6):
        print(*i)
    print()
