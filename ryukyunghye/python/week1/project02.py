'''PROJECT02 컴퓨터의 외부 및 내부 IP 확인
자신의 컴퓨터의 외부 및 내부 IP를 확인할 수 있는 코드를 만들어 봅시다. 
가상 환경 등으로 내부의 IP가 변경되더라도 정확한 IP를 찾을 수 있는 방법에 대해서도 알아봅니다.
'''
import socket                                  # 컴퓨터가 연결된 접속 정보 받아올 때 사용하는 모듈 불러오기
import requests                                # 사이트 접속을 위한 모듈
import re                                      # IP 주소를 찾기 위한 정규식을 사용하기 위한 모듈

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 소켓 연결
in_addr.connect(("www.google.co.kr", 443))     # https의 기본 접속 포트는 443
print("내부IP: ",in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
# 정규식 표현을 사용해 IP주소 가져와 outAddr 변수와 바인딩 함
# 바인딩 : 프로그램의 어떤 기본 단위가 가질 수 있는 구성요소의 구체적인 값을 확정하는 것
print("외부IP: ",out_addr)