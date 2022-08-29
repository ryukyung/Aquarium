# [1525] 퍼즐
import sys
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        now = queue.popleft()
        if now == "123456789":
            return countDict[now]
        space = now.find("9")
        x = space // 3
        y = space % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                nSpace = nx * 3 + ny
                move = list(now)
                move[nSpace], move[space] = move[space], move[nSpace]
                move = "".join(move)

                if not countDict.get(move):
                    queue.append(move)
                    countDict[move] = countDict[now] + 1


start = ""
for _ in range(3):
    temp = sys.stdin.readline().strip()
    temp = temp.replace(" ", "")
    start += temp

start = start.replace("0", "9")
queue = deque()
queue.append(start)

# 이동된 상태, 이동횟수 저장
countDict = dict()
countDict[start] = 0

# 이동이 불가하면 "-1"을 출력
result = bfs()
print(result if result != None else "-1")
