'''PROJECT07. 환율 변환기
환율 정보를 받아 환율을 변환하는 프로그램을 만들어봅시다
'''
import requests
from bs4 import BeautifulSoup
def get_exchange_rate(target1, target2):
    header ={
        'User-Agent' : 'Mozilla/5.0', 'Content-Type' : 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=harders)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'id' : 'last_last'})
    print(containers.text)

get_exchange_rate('usd','krw')