# [9466] 텀 프로젝트
import sys
sys.setrecursionlimit(111111)


def dfs(a):
    global result
    visited[a] = True
    graph.append(a)
    number = numberList[a]

    if visited[number]:
        if number in graph:
            result += graph[graph.index(number):]
        return
    else:
        dfs(number)


t = int(input())
for _ in range(t):
    n = int(input())
    numberList = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            graph = []
            dfs(i)

    print(n - len(result))
