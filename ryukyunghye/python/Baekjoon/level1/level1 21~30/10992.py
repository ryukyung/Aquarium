# [10992] 별 찍기-17
num = int(input())
print(" "*(num-1)*"*")
if(num != 1):
    for i in range(1, num-1):
        print(" "*(num-i-1)+"*"+" "*(2*i-1)+"*")
    print("*"*(2*num-1))
