# [2873] 롤러코스터

r, c = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(r)]
if r % 2 == 1:
    print(("R" * (c - 1) + "D" + "L" * (c - 1) + "D") * (r // 2) + "R" * (c - 1))
elif c % 2 == 1:
    print(("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * (c // 2) + "D" * (r - 1))
elif r % 2 == 0 and c % 2 == 0:
    lowest = 1001  # 가장 작은 값
    lowPosition = [-1, -1]  # 가장 작은 값의 위치
    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if lowest > Map[i][j]:
                    lowest = Map[i][j]
                    lowPosition = [i, j]
        else:
            for j in range(0, c, 2):
                if lowest > Map[i][j]:
                    lowest = Map[i][j]
                    lowPosition = [i, j]
    result = ("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * \
        (lowPosition[1] // 2)
    x = 2 * (lowPosition[1] // 2)
    y = 0
    xTable = 2 * (lowPosition[1] // 2) + 1
    while x != xTable or y != r - 1:
        if x < xTable and [y, xTable] != lowPosition:
            x += 1
            result += 'R'
        elif x == xTable and [y, xTable - 1] != lowPosition:
            x -= 1
            result += 'L'
        if y != r - 1:
            y += 1
            result += 'D'

    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * \
        ((c - lowPosition[1] - 1) // 2)

    print(result)
