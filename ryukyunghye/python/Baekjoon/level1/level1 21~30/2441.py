# [2441] 별 찍기-4
num = int(input())
for i in range(num, 0, -1):
    print(" "*(num-i)+"*"*i)
