import sys
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def divideIsland(i, j):
    global count
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    Map[i][j] = count

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and Map[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                Map[nx][ny] = count
                queue.append([nx, ny])


def shortDistance(z):
    global result
    distance = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if Map[i][j] == z:
                q.append([i, j])
                distance[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if Map[nx][ny] > 0 and Map[nx][ny] != z:
                result = min(result, distance[x][y])
                return
            if Map[nx][ny] == 0 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny])


n = int(sys.stdin.readline())

Map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 1
result = sys.maxsize

for i in range(n):
    for j in range(n):
        if not visited[i][j] and Map[i][j] == 1:
            divideIsland(i, j)
            count += 1


for i in range(1, count):
    shortDistance(i)

print(result)
