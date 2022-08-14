# [10866] 덱
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
Deque = deque()

for _ in range(n):
    order = list(input().split())
    if order[0] == 'push_front':
        Deque.appendleft(order[1])  # 정수를 덱의 앞에_left
    elif order[0] == 'push_back':   # 정수를 덱의 뒤에
        Deque.append(order[1])
    elif order[0] == 'pop_front':
        if len(Deque) == 0:
            print(-1)               # 정수 값이 없다면 -1 출력
        else:
            print(Deque.popleft())  # 덱의 가장 앞에 있는 수를 빼고_popleft()
    elif order[0] == 'pop_back':
        if len(Deque) == 0:
            print(-1)               # 정수가 없다면 -1 출력
        else:
            print(Deque.pop())      # 가장 뒤에 있는 수 제거
    elif order[0] == 'size':
        print(len(Deque))           # 덱에 들어잇는 정수의 개수 출력
    elif order[0] == 'empty':
        if len(Deque) == 0:
            print(1)                # 정수가 없다면 1 출력
        else:
            print(0)                # 정수가 있다면 0 출력
    elif order[0] == 'front':
        if len(Deque) == 0:
            print(-1)               # 정수가 없다면 -1 출력
        else:
            print(Deque[0])         # 덱의 가장 앞에 있는 수 출력
    elif order[0] == 'back':
        if len(Deque) == 0:
            print(-1)               # 정수가 없다면 -1 출력
        else:
            print(Deque[-1])        # 덱의 가장 뒤에 있는 정수 출력
