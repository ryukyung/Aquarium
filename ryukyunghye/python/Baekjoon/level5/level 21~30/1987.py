# [1987] 알파벳
# python - 시간초과, Pypy - O
r, c = map(int, input().split())
table = []
for _ in range(r):
    table.append(list(input()))

result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
alpha = set()


def dfs(x, y, count):
    global result
    result = max(result, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not table[nx][ny] in alpha:
            alpha.add(table[nx][ny])
            dfs(nx, ny, count+1)
            alpha.remove(table[nx][ny])


alpha.add(table[0][0])
dfs(0, 0, 1)
print(result)
