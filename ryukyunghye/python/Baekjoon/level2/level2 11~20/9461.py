# [9461] 파도반 수열
T = int(input())
data = [1, 1, 1, 2, 2]
for i in range(5, 100):
    data.append(data[i-1]+data[i-5])
for _ in range(T):
    n = int(input())
    print(data[n-1])
