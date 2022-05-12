# [2439] 별 찍기-2
num = int(input())
for i in range(1, num+1):
    print(" "*(num-i) + "*"*i)

# [2440] 별 찍기-3
num = int(input())
for i in range(num, 0, -1):
    print("*"*i)

# [2441] 별 찍기-4
num = int(input())
for i in range(num, 0, -1):
    print(" "*(num-i)+"*"*i)

# [2442] 별 찍기-5
num = int(input())
for i in range(1, num+1):
    print(" " * (num-i)+"*"*((i*2)-1))

# [2445] 별 찍기-8
num = int(input())
for i in range(1, num):
    print("*"*i+" "*2*(num-i)+"*"*i)
for i in range(num, 0, -1):
    print("*"*i+" "*2*(num-i)+"*"*i)

# [2446] 별 찍기-9
num = int(input())
for i in range(num):
    print(" "*i+"*"*((num-i)*2-1))
for i in range(num-2, -1, -1):
    print(" "*i+"*"*((num-i)*2-1))

# [10991] 별 찍기-16
num = int(input())
for i in range(1, num+1):
    print(" "*(num-i)+"* "+"*")

# [10992] 별 찍기-17
num = int(input())
print(" "*(num-1)*"*")
if(n != 1):
    for i in range(1, num-1):
        print(" "*(num-i-1)+"*"+" "*(2*i-1)+"*")
    print("*"*(2*num-1))

# [1463] 1로 만들기
# 앞에서 사용했던 결과를 가져와서 사용함 -> 재귀함수 사용
num = int(input())
d = [0]*(num+1)
for i in range(2, num+1):
    d[i] = d[i-1]+1
    if(i % 3 == 0):
        d[i] = min(d[i], d[i//3]+1)
    if(i % 2 == 0):
        d[i] = min(d[i], d[i//2]+1)
print(d[num])
