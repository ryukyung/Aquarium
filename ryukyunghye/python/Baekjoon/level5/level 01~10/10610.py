# [10610] 30

# 방법1
findNumber = list(input())
findNumber.sort(reverse=True)
total = 0
if '0' not in findNumber:
    print(-1)
else:
    for i in findNumber:
        total += int(i)
    if total % 3 != 0:
        print(-1)
    else:
        print(''.join(findNumber))

# 방법2
findNumber = list(input())
findNumber.sort(reverse=True)
total = 0
for i in findNumber:
    total += int(i)
if '0' not in findNumber or total % 3 != 0:
    print(-1)
else:
    print(''.join(findNumber))
