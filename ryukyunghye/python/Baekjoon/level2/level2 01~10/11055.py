# [11055] 가장 큰 바이토닉 부분 수열
n = int(input())
data = list(map(int, input().split()))
dp = data[:]
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[i]+data[i])
print(max(dp))
