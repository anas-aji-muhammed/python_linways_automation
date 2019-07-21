import pyautogui
import time
import webbrowser
webbrowser.open_new_tab('https://mes.linways.com/student/')
#pyautogui.click(207, 64)
#pyautogui.typewrite("https://mes.linways.com/student/")
#pyautogui.typewrite(["enter"])

time.sleep(3)

#Username filling position x=1238 y=488

pyautogui.click(1238, 488)
pyautogui.typewrite("")

#Password filling position x=1254 y=556

pyautogui.click(1254, 556)
pyautogui.typewrite("")

#signin button position x=1505 y=614
pyautogui.click(1505, 614)

time.sleep(2)

#press attendance button x=98 y=831
pyautogui.click(98, 831)
time.sleep(1)

#select attendance x=1030 y=555
pyautogui.doubleClick(1030, 555)
pyautogui.hotkey('ctrl', 'c')


#for logout
pyautogui.click(1864, 162)
pyautogui.click(1769, 304)
time.sleep(2)
pyautogui.hotkey('ctrl', 't')
pyautogui.click(207, 64)
pyautogui.hotkey('ctrl', 'v')