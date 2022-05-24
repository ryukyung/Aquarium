# [11726] 2Xn 타일링
# dp[n] = dp[n-1]+dp[n-2]
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
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])

# [10844] 쉬운 계단 수
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)

# [11057] 오르막 수
n = int(input())
MOD = 10007
dp = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]
            print(sum(dp[n]) % MOD)
