import pyautogui
import webbrowser
import time
from datetime import datetime

while True:
    now = datetime.now()
    if now.strftime("%H%M") == "2120":
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/pnz-hyap-pxb")

        time.sleep(1)
        pyautogui.moveTo(1750, 148)
        pyautogui.click()

        time.sleep(2)
        pyautogui.moveTo(909, 694, )
        pyautogui.click()

        time.sleep(5)
        pyautogui.hotkey('ctrl', 'd')
        pyautogui.hotkey('ctrl', 'e')

        time.sleep(3)
        pyautogui.moveTo(1425, 582)
        pyautogui.click()
        break