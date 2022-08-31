# [2632] 피자판매
import sys

size = int(sys.stdin.readline().rstrip())
countA, countB = map(int, sys.stdin.readline().split())
sliceA = [int(sys.stdin.readline().rstrip()) for _ in range(countA)]
sliceB = [int(sys.stdin.readline().rstrip()) for _ in range(countB)]

totalA, totalB = [0]*2000001, [0]*2000001
totalA[0] = totalB[0] = 1
lenA, lenB = len(sliceA), len(sliceB)
for i in range(lenA):
    temp = 0
    for j in range(lenA):
        temp += sliceA[(i+j) % countA]
        if temp > size:
            break
        else:
            totalA[temp] += 1
for i in range(lenB):
    temp = 0
    for j in range(lenB):
        temp += sliceB[(i+j) % countB]
        if temp > size:
            break
        else:
            totalB[temp] += 1
totalA[sum(sliceA)] = totalB[sum(sliceB)] = 1

result = 0
for i in range(size+1):
    result += (totalA[i] * totalB[size-i])
print(result)
