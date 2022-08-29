# [1451] 직사각형으로 나누기
n, m = map(int, input().split())
square = [[0 for _ in range(m+1)]]
result = 0
for _ in range(n):
    squareNumber = [0] + list(map(int, list(input())))
    square.append(squareNumber)
total = [[0 for _ in range(m+1)] for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, m+1):
        total[x][y] = total[x-1][y] + total[x][y-1] - \
            total[x-1][y-1] + square[x][y]


def calculate(x1, y1, x2, y2):
    return total[x2][y2] - total[x2][y1-1] - total[x1-1][y2] + total[x1-1][y1-1]


# 세로만
for i in range(1, m-1):
    for j in range(i+1, m):
        s1 = calculate(1, 1, n, i)
        s2 = calculate(1, i+1, n, j)
        s3 = calculate(1, j+1, n, m)
        if result < s1*s2*s3:
            result = s1*s2*s3

# 2. 가로만
for i in range(1, n-1):
    for j in range(i+1, n):
        s1 = calculate(1, 1, i, m)
        s2 = calculate(i+1, 1, j, m)
        s3 = calculate(j+1, 1, n, m)
        if result < s1*s2*s3:
            result = s1*s2*s3

# 3. 세로: 세로+가로
for i in range(1, m):
    for j in range(1, n):
        s1 = calculate(1, 1, n, i)
        s2 = calculate(1, i+1, j, m)
        s3 = calculate(j+1, i+1, n, m)
        if result < s1*s2*s3:
            result = s1*s2*s3

# 4. 세로: 가로+세로
for i in range(1, n):
    for j in range(1, m):
        s1 = calculate(1, 1, i, j)
        s2 = calculate(i+1, 1, n, j)
        s3 = calculate(1, j+1, n, m)
        if result < s1*s2*s3:
            result = s1*s2*s3

# 5. 가로: 세로+가로
for i in range(1, n):
    for j in range(1, m):
        s1 = calculate(1, 1, i, m)
        s2 = calculate(i+1, 1, n, j)
        s3 = calculate(i+1, j+1, n, m)
        if result < s1*s2*s3:
            result = s1*s2*s3

# 6. 가로: 가로+세로
for i in range(1, n):
    for j in range(1, m):
        s1 = calculate(1, 1, i, j)
        s2 = calculate(1, j+1, i, m)
        s3 = calculate(i+1, 1, n, m)
        if result < s1*s2*s3:
            result = s1*s2*s3

print(result)
