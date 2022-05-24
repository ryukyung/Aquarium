# [2193] 이친수
n = int(input())
dp = [0, 1, 1]
for i in range(3, 91):
    dp.append(dp[i-2]+dp[i-1])
print(dp[n])

# [9465] 스티커
T = int(input())
for i in range(T):
    dp = []
    n = int(input())
    for j in range(2):
        dp.append(list(map(int, input().split())))
    for k in range(1, n):
        if k == 1:
            dp[0][k] += dp[1][k-1]
            dp[1][k] += dp[0][k-1]
        else:
            dp[0][k] += max(dp[1][k-1], dp[1][k-2])
            dp[1][k] += max(dp[0][k-1], dp[0][k-2])
    print(max(dp[0][n-1], dp[1][n-1]))

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

# [11053] 가장 긴 증가하는 부분 수열
A = int(input())
Ai = list(map(int, input().split()))
dp = [1] * A

for i in range(A):
    for j in range(i):
        if Ai[j] < Ai[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# [11055] 가장 큰 바이토닉 부분 수열
A = int(input())
Ai = list(map(int, input().split()))
dp = Ai[:]
for i in range(A):
    for j in range(i):
        if Ai[i] > Ai[j]:
            dp[i] = max(dp[i], dp[j]+Ai[i])
print(max(dp))
