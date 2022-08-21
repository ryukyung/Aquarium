# [1780] 종이의 개수
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
minus = 0
zero = 0
plus = 0


def dividePaper(x, y, n):
    global minus, zero, plus
    checkNumber = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != checkNumber:
                for k in range(3):
                    for l in range(3):
                        dividePaper(x+k*n//3, y+l*n//3, n//3)
                return None
    if checkNumber == -1:
        minus += 1
    elif checkNumber == 0:
        zero += 1
    else:
        plus += 1


dividePaper(0, 0, n)
print(minus, zero, plus, sep='\n')
