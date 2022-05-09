# [11719] 그대로 출력하기2
while True:
    try:
        string = input()
        print(string)
    except:
        break

# [11720] 숫자의 합
count = int(input())
num = list(input())
total = 0
for i in num:
    total += int(i)
print(total)

# [11721] 열 개씩 끊어 출력하기
a = input()
for i in range(0, len(a), 10):
    print(a[i:i+10])

# [2741] N 찍기
num = int(input())
for i in range(num):
    print(i+1)

# [2742] 기찍 N
num = int(input())
for i in range(num, 0, -1):
    print(i)

# [2739] 구구단
n = int(input())
for i in range(1, 10):
    print('{} * {} = {}'.format(n, i, n*i))

# [1924] 2007년
m, d = map(int, input().split())
day = 0
dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(m-1):  # 리스트는 0부터 시작이라 1을 빼준거임
    day = day + dayList[i]
day = (day+d) % 7
print(weekList[day])

# [8393] 합
num = int(input())
total = 0
for i in range(num+1):
    total += i
print(total)

# [10818] 최소, 최대
count = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))

# [2438] 별 찍기 -1
num = int(input())
for i in range(1, num+1):
    print('*'*i)
