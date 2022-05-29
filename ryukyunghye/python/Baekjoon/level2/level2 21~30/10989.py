
# [10989] 수 정렬하기3
import sys
# n = int(sys.stdin.readline())
# data = []
# for _ in range(n):
#     data.append(int(sys.stdin.readline().split()))
# sorted_data = sorted(data)
# for i in sorted_data:
#     print(i)
# 메모리 초과

n = int(sys.stdin.readline())
data = [0] * 10001
for _ in range(n):
    data[int(sys.stdin.readline())] += 1
for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)
