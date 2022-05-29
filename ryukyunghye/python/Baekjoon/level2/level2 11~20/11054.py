# [11054] 가장 긴 바이토닉 부분 수열
n = int(input())
data = list(map(int, input().split()))
reverse_data = data[::-1]
up = [1 for i in range(n)]
down = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            up[i] = max(up[i], up[j]+1)
        if reverse_data[i] > reverse_data[j]:
            down[i] = max(down[i], down[j]+1)
result = [0 for i in range(n)]
for i in range(n):
    result[i] = up[i] + down[n-i-1] - 1
print(max(result))
