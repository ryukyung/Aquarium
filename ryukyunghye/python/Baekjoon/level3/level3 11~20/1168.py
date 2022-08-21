# [1168] 요세푸스 문제2
# pypy3에서도 시간초과 발생 -> 다시 풀어봐야 함

n, k = map(int, input().split())
peopleTable = []
removeOrder = []
for i in range(1, n+1):
    peopleTable.append(i)
point = 0
for _ in range(n):
    point += k-1
    point %= len(peopleTable)
    removeOrder.append(str(peopleTable.pop(point)))

print("<"+", ".join(removeOrder) + ">")
