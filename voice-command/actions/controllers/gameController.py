import pyautogui
import time
import cv2
import os
print("Working dir:", os.getcwd())
print("Files in here:", os.listdir("."))

pyautogui.FAILSAFE = False

def call():
    pyautogui.click(790, 910)
    time.sleep(1)

def fold():
    pyautogui.click(1290, 910)
    time.sleep(1)

def Bet_Min():
    pyautogui.click(625, 910)
    time.sleep(1)
    pyautogui.click(620, 890)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)

def Bet_1_in_4():
    pyautogui.click(625, 910)
    time.sleep(1)
    pyautogui.click(720, 890)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)

def Bet_1_in_2():
    pyautogui.click(625, 910)
    time.sleep(1)
    pyautogui.click(815, 890)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)

def Bet_3_in_4():
    pyautogui.click(625, 910)
    time.sleep(1)
    pyautogui.click(915, 890)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)

def Bet_All_in():
    pyautogui.click(625, 910)
    time.sleep(1)
    pyautogui.click(1015, 890)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)
    pyautogui.click(1175, 822)
    time.sleep(1)
