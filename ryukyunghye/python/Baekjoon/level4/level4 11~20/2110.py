# [2110] 공유기 설치
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
housePosition = []
for _ in range(n):
    housePosition.append(int(input()))

housePosition.sort()


def binary_search(housePosition, start, end):
    while start <= end:
        middle = (start+end)//2
        install = housePosition[0]
        installCount = 1

        for i in range(1, n):
            if housePosition[i] >= install + middle:
                install = housePosition[i]
                installCount += 1

        if installCount >= c:
            global result
            start = middle + 1
            result = middle
        else:
            end = middle - 1


start = 1
end = housePosition[-1] - housePosition[0]
result = 0
binary_search(housePosition, start, end)
print(result)
