# [11729] 하노이 탑 이동 순서
n = int(input())


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)


result = 1
for i in range(n-1):
    result = result * 2+1
print(result)
hanoi(n, 1, 2, 3)
