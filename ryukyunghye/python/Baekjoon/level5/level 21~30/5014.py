# [5014] 스타트링크
from collections import deque


def bfs(i):
    queue = deque([i])
    visited[i] = 1
    while queue:
        i = queue.popleft()
        if i == arrive:
            return table[arrive]
        for j in (i+up, i-down):
            if 0 < j <= total and not visited[j]:
                visited[j] = 1
                table[j] = table[i] + 1
                queue.append(j)
    if table[arrive] == 0:
        return "use the stairs"


total, now, arrive, up, down = map(int, input().split())
visited = [0 for _ in range(total + 1)]
table = [0 for _ in range(total + 1)]
print(bfs(now))
