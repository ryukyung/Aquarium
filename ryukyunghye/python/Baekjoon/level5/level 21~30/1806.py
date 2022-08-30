# [1806] 부분합
n, s = map(int, input().split())
numberList = list(map(int, input().split()))
i = 0
j = 0
result = 100001
numberListStart = numberList[0]
while True:
    if numberListStart >= s:
        numberListStart -= numberList[i]
        result = min(result, j-i+1)
        i += 1
    else:
        j += 1
        if j == n:
            break
        numberListStart += numberList[j]

if result == 100001:
    print(0)
else:
    print(result)
