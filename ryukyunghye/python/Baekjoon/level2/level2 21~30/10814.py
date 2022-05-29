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
