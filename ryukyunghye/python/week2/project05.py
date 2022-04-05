'''PROJECT05 컴퓨터의 정보 확인
CPU, 메모리, 디스크, 네트워크 등의 정보를 확인하는 컴퓨터의 정보를 확인하는 프로그램을 만들어 봅시다.
1초당 반복해서 정보를 출력하는 코드 만들기
1초에 한 번씩 반복하여 cpu의 사용량, 사용 가능한 메모리, 네트워크 사용량을 출력'''
import psutil
curr_sent = 0
curr_recv = 0
prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1) # cpu의 사용량을 1초동안의 평균값을 구함, interval_1초동안 측정한 후 다음 줄로 이동
    print(f'CPU사용량 : {cpu_p}%') # cpu의 사용량 출력
    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3,1) # 1024를 3번 곱함
    print(f'사용 가능한 메모리 : {memory_avail}GB')
    # 사용 가능한 메모리 출력
    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent, 1) # 현재 측정한 값에서 이전에 측정한 값을 빼면 1초 동안 보내는 데이터
    recv = round(curr_recv-prev_recv, 1) # 현재 측정한 값에서 이전에 측정한 값을 빼면 1초 동안 받은 데이터

    print(f'보내기 : {sent}MB 받기 : {recv}MB')
    # 네트워크에서 보내고 받은 크기 출력
    prev_sent=curr_sent     # 이전의 값에 현재 값을 바인딩, 이전의 값을 가지고 있어야 현재값과 비교해서
    prev_recv = curr_recv   # 1초 동안 얼마를 보내고 받았는지 알 수 있음