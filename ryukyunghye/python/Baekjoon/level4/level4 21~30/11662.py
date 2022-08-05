# [11662] 민호와 강호
def three_search(start, end):
    while abs(end - start) > 1e-9:
        mid1 = (2 * start + end) / 3
        mid2 = (start + 2 * end) / 3
        if distance(mid1) > distance(mid2):
            start = mid1
        else:
            end = mid2
    return distance(start)


def distance(i):
    minX = ax * i + bx * (1 - i)
    minY = ay * i + by * (1 - i)
    kangX = cx * i + dx * (1 - i)
    kangY = cy * i + dy * (1 - i)
    return ((kangX - minX) ** 2 + (kangY - minY) ** 2) ** 0.5


ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
print(round(three_search(0, 1), 16))
