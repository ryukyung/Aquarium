# [1912] 연속 합
n = int(input())
list = list(map(int, input().split()))
dp = [0]*n
dp[0] = list[0]
for i in range(1, n):
    dp[i] = max(list[i], dp[i-1]+list[i])
print(max(dp))
