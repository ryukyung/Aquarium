# [11726] 2Xn 타일링
import sys
n = int(input())
dp = [0 for _ in range(n+1)]
if n <= 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[i] % 10007)

# [11727] 2Xn 타일링2
n = int(input())
dp = [0, 1, 3]
for i in range(3, n+1):
    dp.append((dp[i-1])+((dp[i-2]*2)))
print(dp[n] % 10007)

# [9095] 1,2,3 더하기
T = int(input())


def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)


for i in range(T):
    n = int(input())
    print(sol(n))

# [10844] 쉬운 계단 수
n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
            # 0이니깐 뒤에 1만 오지
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
            # 9니깐 뒤에 8만 오는 거임
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)

# [11057] 오르막 수
n = int(input())
dp = [1]*10
for _ in range(n):
    dp.append(list[0]*10)
for i in range(1, n+1):
    for j in range(0, 10):
        for col in range(j+1):
            dp[i][j] += dp[i-1][col]
print(dp[n][9] % 10007)
