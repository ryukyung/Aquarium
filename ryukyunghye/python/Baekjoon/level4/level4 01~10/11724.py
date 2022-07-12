# [11724] 연결 요소의 개수
'''
간단히 연결된 노드들을 간선을 따라 dfs나 bfs로 돌면서
방문한 노드들은 방문 기록을 남기면 됨
간선을 따라 연결된 노드들을 다 돌고 나서 dfs나 bfs를
한 번 빠져나올 때마다 카운트를 1씩 증가시켜서
총 몇 번 도는지만 체크하면 되는 방문
'''
# 방법1 - dfs 사용
from collections import deque
import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
# 방법2 - bfs 사용


def bfs(startPoint):
    queue = deque([startPoint])
    visited[startPoint] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        visited[i] = True
    else:
        bfs(i)
        count += 1
print(count)
