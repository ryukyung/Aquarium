# [11005] 진법 변환2
decimalNumber, xNumber = map(int, input().split())
result = ''
pin = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while decimalNumber != 0:
    result += str(pin[decimalNumber % xNumber])
    decimalNumber //= xNumber
print(result[::-1])
