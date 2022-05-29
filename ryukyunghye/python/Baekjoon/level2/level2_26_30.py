import sys

# [10989] 수 정렬하기3
# n = int(sys.stdin.readline())
# data = []
# for _ in range(n):
#     data.append(int(sys.stdin.readline().split()))
# sorted_data = sorted(data)
# for i in sorted_data:
#     print(i)
# 메모리 초과

n = int(sys.stdin.readline())
data = [0] * 10001
for _ in range(n):
    data[int(sys.stdin.readline())] += 1
for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)


# [11652] 카드
n = int(input())
dic = {}
for case in range(n):
    card = int(input())
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])

# [11004] k번째 수
n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
print(data[k-1])

# [10828] 스택
N = int(sys.stdin.readline())
# N = int(input())
stack = []
for _ in range(N):
    # word = input().split()
    word = sys.stdin.readline().split()
    order = word[0]
    if order == "push":
        value = word[1]
        stack.append(value)
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


# [9012] 괄호
T = int(input())
for i in range(T):
    a = list(input())
    sum = 0
    for i in a:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
