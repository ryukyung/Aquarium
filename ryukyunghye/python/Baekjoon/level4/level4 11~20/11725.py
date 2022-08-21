# [11725] 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)


def dfs(x):
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = x
            dfs(i)


dfs(1)

for i in range(2, n+1):
    print(visited[i])
