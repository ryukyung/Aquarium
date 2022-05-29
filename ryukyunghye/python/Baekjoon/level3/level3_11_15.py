# [1406] 에디터
N = list(input())
cursor = len(N)
for i in range(int(input())):
    command = list(input().split())
    if command[0] == 'P':
        N.insert(cursor, command[1])
    elif command[0] == 'L':
        if cursor >0:
            cursor -=1
    elif command[0] =='D':
        if cursor<len(N):
            cursor +=1
    else:
        if cursor>0:
            N.remove(N[cursor-1])
print(''.join(N))
print(N)


N = list(input())
cursor = len(N)

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'P':
        N.insert(cursor, command[1])
        cursor += 1
  
    elif command[0] == 'L':
        if cursor > 0:
            cursor -= 1

    elif command[0] =='D':
        if cursor < len(N):
            cursor += 1
  
    else:
        if cursor > 0:
            N.remove(N[cursor-1])

print(''.join(N))

# [1158] 요세푸스 문제

# [1168] 요세푸스 문제2

# [10430] 나머지

# [2609] 최대공약수와 최소공배수
