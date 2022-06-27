# [11053] 가장 긴 증가하는 부분 수열
# 방법1
n = int(input())
data = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# 방법2
n = int(input())
number = list(map(int, input().split()))
result = [0] * n
for i in range(n):
    for j in range(i):
        if number[i] > number[j] and result[j] > result[i]:
            result[i] = result[j]
    result[i] += 1
print(max(result))
