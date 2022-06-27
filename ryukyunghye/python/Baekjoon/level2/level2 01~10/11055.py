# [11055] 가장 큰 바이토닉 부분 수열
# 방법1
n = int(input())
data = list(map(int, input().split()))
dp = data[:]
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[i]+data[i])
print(max(dp))

# 방법2
n = int(input())
number = list(map(int, input().split()))
result = [0]*n
result[0] = number[0]
for i in range(1, n):
    for j in range(i):
        if number[i] > number[j]:
            result[i] = max(result[i], result[j]+number[i])
        else:
            result[i] = max(result[i], number[i])
print(max(result))
