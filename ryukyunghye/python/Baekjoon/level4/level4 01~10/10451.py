# [10451] 순열 사이클
import sys
sys.setrecursionlimit(10000)  # 재귀 한도 풀어주기


def dfs(start):
    visited[start] = True
    node = graph[start]
    if not visited[node]:
        dfs(node)


testCase = int(sys.stdin.readline())
for _ in range(testCase):
    n = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False] * n
    result = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)
