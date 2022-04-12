'''PROJECT11 오토마우스를 활용한 PC 카카오톡 자동화
오토마우스를 활요하는 pc에 설치된 카카오톡을 통해 메시지를 자동으로 보내는 프로그램을 만들어봅니다.'''
from copyreg import pickle
from sched import scheduler
from time import time
import pyperclip
import pyautogui
import pyperclip
import time
import schedule


def send_message():
    picPosition = pyautogui.locateOnScreen(r'week3\project11_p1.png')
    print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'wee3\project11_p2.png')
        print(picPosition)
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'week3\project11_p3.png')
        print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy('이 메세지는 자동으로 보내는 메세지 입니다')
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"])
    time.sllep(1.0)


schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
