# [11724] 연결 요소의 개수
import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
result = 0

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            result += 1
            visited[i] = True
        else:
            bfs(i)
            result += 1
print(result)
