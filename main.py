import time
import pyperclip
import pyautogui
import pywhatkit

number = "INSIRA UM NÚMERO AQUI"
pywhatkit.sendwhatmsg_instantly(number, "")
with open("script.txt", "r", encoding="utf-8") as f:
    for line in f:
        pyperclip.copy(line)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        time.sleep(3)
