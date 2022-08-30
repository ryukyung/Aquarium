# [10971] 외판원 순회2
import sys

n = int(input())
travelCost = [list(map(int, input().split())) for _ in range(n)]
minPrice = sys.maxsize


def dfs(startNumber, nextNumber, price, visited):
    global minPrice
    if len(visited) == n:
        if travelCost[nextNumber][startNumber] != 0:
            minPrice = min(minPrice, price+travelCost[nextNumber][startNumber])
        return None
    for i in range(n):
        if travelCost[nextNumber][i] != 0 and i not in visited and price < minPrice:
            visited.append(i)
            dfs(startNumber, i, price+travelCost[nextNumber][i], visited)
            visited.pop()


for i in range(n):
    dfs(i, i, 0, [i])

print(minPrice)
