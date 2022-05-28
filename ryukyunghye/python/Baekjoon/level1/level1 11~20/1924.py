# [1924] 2007년
m, d = map(int, input().split())
day = 0
dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(m-1):  # 리스트의 시작 : 0 -> 1월이 0번지(31), m월을 받으려면 m-1
    day = day + dayList[i]  # day 채우기
day = (day+d) % 7          # day + d = m월을 '일'로 바꾸고 + d, %7: 요일 받기
print(weekList[day])
