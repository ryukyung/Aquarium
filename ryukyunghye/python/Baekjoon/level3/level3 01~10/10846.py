# [10846] 큐
import sys
n = sys.stdin.readline()         # 명령 수 받기
que = []
for i in range(n):
    q = n().split()  # 명령을 하나씩 받음
    if q[0] == 'push':
        que.append(q[1])          # 정수를 큐에 넣는다
    elif q[0] == 'pop':
        if que:
            print(que.pop(0))     # 가장 앞의 정수 빼고 출력
        else:
            print(-1)             # 큐에 들어있는 정수 없으면 -1
    elif q[0] == 'size':
        print(len(que))           # 큐에 들어있는 정수의 개수
    elif q[0] == 'empty':
        if len(que) == 0:
            print(1)              # 큐가 비었으면 1
        else:
            print(0)              # 큐가 안 비었으면 0
    elif q[0] == 'front':
        if len(que) == 0:         # 큐에 들어있는 정수 없으면 -1
            print(-1)
        else:
            print(que[0])         # 큐의 가장 앞에 있는 정수 출력
    elif q[0] == 'back':
        if len(que) == 0:
            print(-1)             # 큐에 들어있는 정수 없으면 -1
        else:
            print(que[-1])        # 큐의 가장 뒤에 있는 정수 출력
