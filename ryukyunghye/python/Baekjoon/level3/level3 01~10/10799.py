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
