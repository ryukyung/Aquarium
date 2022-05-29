# [2011] 암호코드
import sys
n = sys.stdin.readline
data = list(str(sys.stdin.readline().strip()))
dp = [0 for _ in range(len(data)+1)]
dp[0] = 1
dp[1] = 1
if data[0] == '0':
    print(0)
else:
    for i in range(2, len(data)+1):
        if int(data[i-1]) > 0:
            dp[i] += dp[i-1]
        to_int = int(data[i-2]+data[i-1])
        if 10 <= to_int <= 26:
            dp[i] += dp[i-2]
    print(dp[len(data)] % 1000000)
