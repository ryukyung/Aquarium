# [11721] 열 개씩 끊어 출력하기
a = input()
for i in range(0, len(a), 10):
    print(a[i:i+10])
