# [2156] 포도주 시식
# 방법1
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

# 방법2
n = int(input())
dp = []
for i in range(n):
    dp.append(int(input()))
drink = [0]*n
if n > 1:
    drink = dp[0]+dp[1]
if n > 2:
    drink[2] = max(dp[2]+dp[1], dp[2]+dp[0], drink[1])

# 방법3
n = int(input())
array = [0] * 10000
for i in range(n):
    array[i] = int(input())
result = [0]*10000
result[0] = array[0]
result[1] = array[0]+array[1]
result[2] = max(array[2]+result[0], array[2]+array[1], result[1])
for i in range(3, n):
    result[i] = max(array[i]+result[i-2], array[i] +
                    array[i-1]+result[i-3], result[i-1])
print(max(result))
