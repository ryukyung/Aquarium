# 5. [10951] A+B-4
# 방법1
while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
# 방법2
try:
    while 1:
        a, b = map(int, input().split())
        print(a+b)
except:
    exit()
