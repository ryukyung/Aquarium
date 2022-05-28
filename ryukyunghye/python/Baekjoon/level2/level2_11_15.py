# [11722] 가장 긴 감소하는 부분 수열
n = int(input())
data = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if data[j] > data[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# [11054] 가장 긴 바이토닉 부분 수열
# 잠시 생략->2022.05.16
# 2022.05.29. 확인 완료

# [1912] 연속 합
n = int(input())
list = list(map(int, input().split()))
dp = [0]*n
dp[0] = list[0]
for i in range(1, n):
    dp[i] = max(list[i], dp[i-1]+list[i])
print(max(dp))

# [2579] 계단 오르기
n = int(input())
score = [0]
for _ in range(n):
    score.append(int(input()))
if n == 1:
    print(score[1])
else:
    dp = [0]*(n+1)
    dp[1] = score[1]
    dp[2] = score[1]+score[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])
    print(dp[n])

# [1699] 제곱수의 합
n = int(input())
dp = [i for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
print(dp[n])
