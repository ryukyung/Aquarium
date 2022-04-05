'''PROJECT08 쓰레드를 사용한 프로그램
쓰레드란 코드를 실행하는 하나의 동작입니다. 우리는 파이썬 코드를 이용하여 하나의 동작을 하는 코드를 만들고 있습니다.
하지만 프로그램이 커지고 해야 할 일이 많아진다면 하나의 동작만을 가지고는 부족하여 쓰레드라는 방식의 프로그램 방식을 사용하여 동작을 늘릴 수 있습니다.'''
import threading

def sum(name, value): # name과 value를 입력받아 value의 회수만큼 반복함
    for i in range(0, value):
        print(f"{name} : {i}")

t1 = threading.Thread(target = sum, args = ('1번 쓰레드', 10)) # t1 쓰레드 생성, 입력값_name-'1번쓰레드', value_10
t2 = threading.Thread(target = sum, args = ('2번 쓰레드', 10)) # t2 쓰레드 생성, 입력값_name-'2번쓰레드', value_10

t1.start()
t2.start()

print("MAin Thread")