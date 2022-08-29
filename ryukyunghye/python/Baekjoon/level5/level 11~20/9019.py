# [9019] DSLR
# python3 시간초과, pypy3 - O
from collections import deque
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().split())
    queue = deque()
    queue.append((a, ""))
    visited = [False] * 10000

    while queue:
        number, path = queue.popleft()
        visited[number] = True
        if number == b:
            print(path)
            break
        # D
        number2 = (number*2) % 10000
        if not visited[number2]:
            queue.append((number2, path+"D"))
            visited[number2] = True

        # S
        number2 = (number - 1) % 10000
        if not visited[number2]:
            queue.append((number2, path+"S"))
            visited[number2] = True

        # L
        number2 = (number*10 + (number//1000)) % 10000
        if not visited[number2]:
            queue.append((number2, path+"L"))
            visited[number2] = True

        # R
        number2 = (number//10 + (number % 10)*1000) % 10000
        if not visited[number2]:
            queue.append((number2, path+"R"))
            visited[number2] = True
