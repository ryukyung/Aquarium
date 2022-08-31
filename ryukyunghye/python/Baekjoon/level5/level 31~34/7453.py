# [7453] 합이 0인 네 정수
# python - 시간초과, pypy - O
import sys
input = sys.stdin.readline
n = int(input())
aList, bList, cList, dList = [], [], [], []
result = 0
dict = dict()

for _ in range(n):
    a, b, c, d = map(int, input().split())
    aList.append(a)
    bList.append(b)
    cList.append(c)
    dList.append(d)

for a in aList:
    for b in bList:
        temp = a+b
        if temp not in dict.keys():
            dict[temp] = 1
        else:
            dict[temp] += 1

for c in cList:
    for d in dList:
        temp = -1*(c+d)
        if temp in dict.keys():
            result += dict[temp]
print(result)
