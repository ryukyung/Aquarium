# [1963] 소수 경로
import sys
import math
from collections import deque


def primeNumber():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2*i, 10000, i):
                prime[j] = False


def bfs():
    queue = deque()
    queue.append([start, 0])
    visited = [0 for _ in range(10000)]
    visited[start] = 1

    while queue:
        now, count = queue.popleft()

        if now == end:
            return count
        for i in range(4):
            for j in range(10):
                temp = int(str(now)[:i] + str(j)+str(now)[i+1:])
                if visited[temp] == 0 and prime[temp] and temp >= 1000:
                    visited[temp] = 1
                    queue.append([temp, count+1])


testCase = int(input())
prime = [True for _ in range(10000)]
primeNumber()
for _ in range(testCase):
    start, end = map(int, input().split())
    result = bfs()
    if result != None:
        print(result)
    else:
        print("Impossible")
