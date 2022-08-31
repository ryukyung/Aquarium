# [1261] 알고스팟
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
table = [[-1] * m for _ in range(n)]

queue = deque()
queue.append((0, 0))
table[0][0] = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if table[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    table[nx][ny] = table[x][y]
                    queue.appendleft((nx, ny))
                else:
                    table[nx][ny] = table[x][y]+1
                    queue.append((nx, ny))
print(table[n-1][m-1])
