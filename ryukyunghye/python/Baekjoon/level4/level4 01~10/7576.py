# [7576] 토마토
from collections import deque

m, n = map(int, input().split())
tomatoBox = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for i in range(n):
    for j in range(m):
        if tomatoBox[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and tomatoBox[nx][ny] == 0:
                tomatoBox[nx][ny] = tomatoBox[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in tomatoBox:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))
print(result - 1)
