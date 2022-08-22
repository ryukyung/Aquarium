# [2261] 가장 가까운 두  점
import sys

n = int(sys.stdin.readline())
point = []
for _ in range(n):
    point.append(tuple(map(int, sys.stdin.readline().split())))

point = list(set(point))  # set: 중복 제거, 중복된 점의 최솟값은 0
point.sort(key=lambda x: x[0])  # 0번지의 값으로 오름차순


def resultDistance(x, y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2


def solve(z):
    if len(z) == 2:
        return resultDistance(z[0], z[1])
    elif len(z) == 3:
        return min(resultDistance(z[0], z[1]), resultDistance(z[0], z[2]), resultDistance(z[1], z[2]))
    else:
        middle = len(z)//2  # 계속해서 2로 나눔
        shortDistance = min(solve(z[:middle]), solve(z[middle:]))
        temp = []
        for i in range(len(z)):
            if (z[i][0]-z[middle][0]) ** 2 <= shortDistance:
                temp.append(z[i])
        if len(temp) >= 2:
            # 점이 1개면 거리가 없지
            temp.sort(key=lambda x: x[1])
            for i in range(len(temp)-1):
                for j in range(i+1, len(temp)):
                    if(temp[i][1] - temp[j][1])**2 > shortDistance:
                        # y 좌표가 최소거리보다 크면 중지
                        break
                    elif temp[i][0] < z[middle][0] and temp[j][0] < z[middle][0]:
                        # resultDistance(z[:middle])
                        continue
                    elif temp[i][0] >= z[middle][0] and temp[j][0] >= z[middle][0]:
                        # resultDistance(z[middle:])
                        continue
                    shortDistance = min(
                        shortDistance, resultDistance(temp[i], temp[j]))
        return shortDistance


if n != len(point):
    print(0)
else:
    print(solve(point))
