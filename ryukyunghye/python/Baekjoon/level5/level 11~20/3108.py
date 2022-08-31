# [3108] 로고
from collections import deque
import sys
n = int(sys.stdin.readline())
graph = [[0]*2001 for _ in range(2001)]
table = [[0]*2001 for _ in range(2001)]
start = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue.append([x, y])
    table[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000:
                if graph[nx][ny] == 1 and table[nx][ny] == 0:
                    table[nx][ny] = 1
                    queue.append([nx, ny])


for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 = (x1+500)*2
    y1 = (y1+500)*2
    x2 = (x2+500)*2
    y2 = (y2+500)*2
    start.append([x1, y1])
    for i in range(x1, x2+1):
        if i == x1 or i == x2:
            for j in range(y1, y2+1):
                graph[i][j] = 1
        else:
            graph[i][y1] = 1
            graph[i][y2] = 1

queue = deque()
result = 0
for i in range(len(start)):
    x, y = start[i]
    if table[x][y] == 0:
        bfs(x, y)
        result += 1

if graph[1000][1000] == 1:
    result -= 1
print(result)
