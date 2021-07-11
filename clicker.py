# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyautogui
import time
import schedule
import datetime


pyautogui.FAILSAFE = False

def clickBell():
    # # 좌표 객체 얻기 
    # position = pyautogui.position()
    # # x, y 좌표
    # print(position.x)
    # print(position.y) 
    # # 화면 전체 크기 확인하기
    # print(pyautogui.size())
    print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " ClickBell")
    # 마우스 이동 (x 좌표, y 좌표)
    pyautogui.moveTo(1781, 238)
    # 마우스 클릭
    pyautogui.click()
    time.sleep(2)
    
    # 마우스 이동 (x 좌표, y 좌표)
    pyautogui.moveTo(573, 1066)
    # 마우스 클릭
    pyautogui.click()
    
# schedule.every(8).seconds.do(clickBell) #30분마다 실행
schedule.every(10).minutes.do(clickBell) #30분마다 실행
 
#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(2)


