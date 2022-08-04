# [1783] 병든 나이트
dy, dx = map(int, input().split())
if dy == 1:
    print(1)
elif dy == 2:
    print(min(4, (dx+1)//2))
else:
    if dx <= 6:
        print(min(4, dx))
    else:
        print(dx-2)
