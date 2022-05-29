# [2156] 포도주 시식
n = int(input())
dp = []
for i in range(n):
    dp.append(int(input()))
list0 = [0]*n
list0[0] = dp[0]
if n > 1:
    list0[1] = dp[0]+dp[1]
if n > 2:
    list0[2] = max(dp[2]+dp[1], dp[2]+dp[0], list0[1])
for i in range(3, n):
    list0[i] = max(list0[i-1], list0[i-3]+dp[i-1]+dp[i], list0[i-2]+dp[i])
print(list0[n-1])

n = int(input())
dp = []
for i in range(n):
    dp.append(int(input()))
drink = [0]*n
if n > 1:
    drink = dp[0]+dp[1]
if n > 2:
    drink[2] = max(dp[2]+dp[1], dp[2]+dp[0], drink[1])
