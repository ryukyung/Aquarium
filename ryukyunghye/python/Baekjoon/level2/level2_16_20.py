# [2133] 타일 채우기
# 2022.05.20 -> 일단 포기! 다음에 다시 도전
import sys
n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i-2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i-j]
    dp[i] += 2
print(dp[n])

n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
print(dp[n])


# [9461] 파도반 수열
T = int(input())
data = [1, 1, 1, 2, 2]
for i in range(5, 100):
    data.append(data[i-1]+data[i-5])
for _ in range(T):
    n = int(input())
    print(data[n-1])

# [2225] 합분해


def input(): return sys.stdin.readline().strip()


n, k = map(int, input().split())
dp = [[0] * 201 for i in range(201)]
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1
for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000
print(dp[k][n])

# [2011] 암호코드
n = sys.stdin.readline
data = list(str(sys.stdin.readline().strip()))
dp = [0 for _ in range(len(data)+1)]
dp[0] = 1
dp[1] = 1
if data[0] == '0':
    print(0)
else:
    for i in range(2, len(data)+1):
        if int(data[i-1]) > 0:
            dp[i] += dp[i-1]
        to_int = int(data[i-2]+data[i-1])
        if 10 <= to_int <= 26:
            dp[i] += dp[i-2]
    print(dp[len(data)] % 1000000)


# [11052] 카드 구매보기
n = int(input())
data = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+data[j])
print(dp[i])
