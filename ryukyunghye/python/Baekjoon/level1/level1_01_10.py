# 1. [2557] Hello World
print("Hello World!")

# 2. [1000] A+B
a, b = input().split()
print(int(a)+int(b))

# 3. [2558] A+B-2
a = int(input())
b = int(input())
print(a+b)

# 4. [10950] A+B-3
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a+b)

# 5. [10951] A+B-4
# 방법1
while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
# 방법2
try:
    while 1:
        a, b = map(int, input().split())
        print(a+b)
except:
    exit()

# 6. [10952] A+B-5
while True:
    a, b = map(int, input().split())
    if((a == 0) and (b == 0)):
        break
    else:
        print(a+b)

# 7. [10953] A+B-6
t = int(input())
for i in range(t):
    a, b = map(int, input().split(','))
    print(a+b)

# 8. [11021] A+B-7
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')


# 9. [11022] A+B-8
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')

# 10. [11718] 그대로 출력하기
while True:
    try:
        same = input()
        print(same)
    except:
        break
