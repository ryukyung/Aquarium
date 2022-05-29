# [10799] 쇠막대기
from sys import stdin
stick = input()
stack = []
sum = 0
i = 0
while i < len(stick):
    s = stick[i]
    if s == '(':               # 만약에 괄호를 열었어
        if stick[i+1] == ')':  # 그 뒤에 바로 닫았어
            sum += len(stack)  # 그럼 sum에 더해줘
            i += 1
        else:                  # 만약에 괄호를 또 열었어
            sum += 1
            stack.append(s)    # stack에 괄호 하나를 추가해줘
    else:                      # 만약에 괄호를 닫았어
        stack.pop()            # 열린 거랑 닫은거랑 같이 제거해줘
    i += 1
print(sum)

# [10846] 큐
# 밑에 애가 저장 시 지워짐
# import sys
n = sys.stdin.readline()         # 명령 수 받기
que = []
for i in range(n):
    q = stdin.readline().split()  # 명령을 하나씩 받음
    if q[0] == 'push':
        que.qppend(q[1])          # 정수를 큐에 넣는다
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

# [10866] 덱
#import sys
#from collections import deque
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


# [10808] 알파벳 개수
s = input()
alphabet = [0] * 26
for i in s:
    alphabet[ord(i)-97] += 1
print(*alphabet)

# [10809] 알파벳 찾기
word = input()
alphabet = list(range(97, 97+26))
for i in alphabet:
    print(word.find(chr(i)))
