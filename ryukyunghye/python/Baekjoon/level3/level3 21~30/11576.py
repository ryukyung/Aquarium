# [11576] Base Conversion
a, b = map(int, input().split())
m = int(input())
alist = list(map(int, input().split()))
A = 0
for i in range(m):
    A += alist[m-i-1]*a**i
result = ''
while A:
    result = ' '+result
    result = str(A % b)+result
    A //= b
print(result)
