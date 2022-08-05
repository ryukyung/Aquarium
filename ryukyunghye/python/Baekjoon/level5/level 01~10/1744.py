# [1744] 수 묶기
number = int(input())
positive = []
negative = []
result = 0
for _ in range(number):
    n = int(input())
    if n == 1:
        result += 1
    elif n > 1:
        positive.append(n)
    else:
        negative.append(n)
positive.sort(reverse=True)
negative.sort()

if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        result += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        result += positive[i] * positive[i+1]
    result += positive[-1]

if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        result += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        result += negative[i] * negative[i+1]
    result += negative[-1]
print(result)
