# [2186] 문자판
import sys
n, m, k = map(int, sys.stdin.readline().split())

table = []
for _ in range(n):
    table.append(sys.stdin.readline().rstrip())

word = sys.stdin.readline().rstrip()

visited = [[[-1] * len(word) for _ in range(m)] for _ in range(n)]


def dfs(x, y, index):
    global n, m, k, word
    if visited[x][y][index] != -1:
        return visited[x][y][index]

    if table[x][y] != word[index]:
        return 0
    if index == len(word) - 1:
        return 1
    count = 0
    for i in range(-k, k+1):
        if not i:
            continue
        if 0 <= x+i < n:
            count += dfs(x+i, y, index+1)

        if 0 <= y+i < m:
            count += dfs(x, y+i, index+1)
    visited[x][y][index] = count
    return count


result = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == word[0]:
            result += dfs(i, j, 0)
print(result)
