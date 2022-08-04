# [1931] 회의실 배정
meeting = int(input())
times = [[0]*2 for _ in range(meeting)]

for i in range(meeting):
    start, end = map(int, input().split())
    times[i][0] = start
    times[i][1] = end

times.sort(key=lambda x: (x[1], x[0]))

result = 1
endTime = times[0][1]
for i in range(1, meeting):
    if times[i][0] >= endTime:
        result += 1
        endTime = times[i][1]

print(result)
