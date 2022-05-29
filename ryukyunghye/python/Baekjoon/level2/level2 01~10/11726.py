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
