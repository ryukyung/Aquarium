# [4963] 섬의 개수
import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    # 상하좌우+대각선
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    table[x][y] = 0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= nx < h) and (0 <= ny < w) and table[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    table = []
    result = 0
    for _ in range(h):
        table.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if table[i][j] == 1:
                dfs(i, j)
                result += 1
    print(result)
