# [11399] ATM
people = int(input())
times = list(map(int, input().split()))
result = 0
times.sort()
for i in range(people):
    for j in range(i+1):
        result += times[j]
print(result)
