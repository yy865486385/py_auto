import getwindow
import win32api
import win32gui
import ctypes
import win32con
import pyautogui
import time
from imgmatching import *

hwnd = win32gui.FindWindow(None,'Yu-Gi-Oh! DUEL LINKS')


# hwnd = win32gui.FindWindow(None,'183')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

# getwindow.print_all_win() # 3670784

# position = getwindow.find_win_by_handle(394824)
# print(position)
# game = IsImage(position=position)
game = IsImage(position=(left, top, right, bottom))


# concheck = game.is_img('pic/home.png', 0.9)
# print(concheck)

pos= game.get_coor('pic/pvp.png',0.9)
print(pos)


def click2(x,y):               #第二种
    ctypes.windll.user32.SetCursorPos(x,y)
    ctypes.windll.user32.mouse_event(2,0,0,0,0)
    ctypes.windll.user32.mouse_event(4,0,0,0,0)
    
def doClick(cx,cy):#第四种，可后台
    long_position = win32api.MAKELONG(cx, cy)#模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起


time.sleep(5)
# ctypes.windll.user32.SetCursorPos(300,300)
doClick(int(pos[0]),int(pos[1]))
# count=0
# while(count<10):
#     doClick(1060,610)
#     count+=1
