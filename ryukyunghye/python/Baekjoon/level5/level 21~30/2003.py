# [2003] 수들의 합2
n, m = map(int, input().split())
aList = list(map(int, input().split()))

start, end = 0, 1
result = 0

while end <= n and start <= end:
    totalList = aList[start:end]
    total = sum(totalList)

    if total == m:
        result += 1
        end += 1
    elif total < m:
        end += 1
    else:
        start += 1
print(result)
