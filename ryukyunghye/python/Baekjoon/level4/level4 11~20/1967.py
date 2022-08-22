# [1967] 트리의 지름
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
result = 0
for _ in range(n-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    graph[parent].append((child, weight))


def dfs(n, x):
    left, right = 0, 0
    for node, w in graph[n]:
        i = dfs(node, w)
        if left <= right:
            left = max(left, i)
        else:
            right = max(right, i)

    global result
    result = max(result, left+right)
    return max(left+x, right+x)


dfs(1, 0)
print(result)
