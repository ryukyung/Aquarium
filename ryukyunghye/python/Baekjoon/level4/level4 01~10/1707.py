# [1707] 이분 그래프
import sys
from collections import deque


def bfs(start, group):
    queue = deque([start])
    visited[start] = group
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[a]
            elif visited[i] == visited[a]:
                return False
    return True


k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v + 1)]
    visited = [False] * (v + 1)

    for _ in range(e):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
