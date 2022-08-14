# [2089] -2진수
n = int(input())
if not n:
    print('0')
    exit()
result = ''
while n:
    if n % (-2):
        result = '1' + result
        n = n//(-2) + 1
    else:
        result = '0' + result
        n //= -2
print(result)
