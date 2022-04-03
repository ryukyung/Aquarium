'''PROJECT01 숫자 맞추기 게임 만들기
1부터 100까지의 임의의 수를 생성하고 생성된 임의의 수를 맞추는 게임 프로그램으로 숫자를 하나 입력하면 임의로 생성된 수보다 높은지 낮은지 정답인지를 알려줍니다.
정답을 맞힌 경우 정답을 몇 번 만에 맞추었는지 그 결과로 게임의 승부를 알 수 있습니다.
'''
import random                         # 임의의 수 출력
randomNumber = random.randint(1, 10) # 범위는 1~100인 정수
count = 1                             # 몇 번 만에 맞추는지
while True:                           # 무한루프
    number = int(input("1~100 사이 숫자를 입력하세요 : "))
    if number < randomNumber:         # 임의로 생성된 수보다 낮으면
        print('up')                   # up
    elif number > randomNumber:       # 임의로 생성된 수보다 크면
        print('down')                 # down
    elif number == randomNumber:      # 같으면
        print("{}회 만에 맞췄습니다".format(count))
        # {}에 count값이 들어감
        break                         # 맞췄으니 무한루프 나가기
    count += 1