# [2751] 수 정렬하기2
import sys
n = int(input())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))
for i in sorted(data):
    sys.stdout.write(str(i)+'\n')

# [11650] 좌표 정렬하기
n = int(sys.stdin.readline())
data = []
for i in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    data.append([a, b])
sorted_data = sorted(data)
for i in range(n):
    print(sorted_data[i][0], sorted_data[i][1])

# [11651] 좌표 정렬하기2
n = int(sys.stdin.readline())
data = []
for i in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    data.append([b, a])
sorted_data = sorted(data)
for b, a in sorted_data:
    print(a, b)

# [10814] 나이순 정렬
# lambda 이용한 간단한 정렬임
n = int(input())
data = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    data.append((age, name))
data.sort(key=lambda x: x[0])  # (age, name)에서 age만 비교
for i in data:
    print(i[0], i[1])

# [10825] 국영수
n = int(sys.stdin.readline())
data = [list(sys.stdin.readline().split()) for _ in range(n)]
data.sort(key=lambda a:  (-int(a[1]), int(a[2]), -int(a[3]), a[0]))
for i in data:
    sys.stdout.write(str(i[0])+'\n')
