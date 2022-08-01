# [1654] 랜선 자르기
import sys
ohLan, needLan = map(int, sys.stdin.readline().split())
ohLanList = []  # 오영식이 가지고 있는 랜선 리스트
for _ in range(ohLan):
    ohLanList.append(int(sys.stdin.readline()))
start, end = 1, max(ohLanList)  # 가장 작은 값, 리스트에서 가장 큰 값
while start <= end:  # 조건을 만족하는 최대 랜선 길이 찾기
    middle = (start+end)//2  # 시작과 끝의 중간 지점
    lines = 0  # 만들 랜선의 총 개수
    for i in ohLanList:
        lines += i//middle  # 총 몇 개의 랜선이 나오나
    # 랜선이 목표치 이상/이하면 start=middle+1/end = middle -1
    if lines >= needLan:  # 랜선의 개수가 분기점
        start = middle + 1
    else:
        end = middle - 1
print(end)
