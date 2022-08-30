# [2580] 스도쿠
# python - 시간초과, pypy - O
graph = []
table = []

for _ in range(9):
    graph.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            table.append((i, j))


def checkX(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True


def checkY(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True


def check33(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(index):
    if index == len(table):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = table[index][0]
        y = table[index][1]

        if checkX(x, i) and checkY(y, i) and check33(x, y, i):
            graph[x][y] = i
            dfs(index+1)
            graph[x][y] = 0


dfs(0)
