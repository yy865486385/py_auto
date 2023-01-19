import win32gui
import win32api
import pyautogui



ygodl_title = "Yu-Gi-Oh! DUEL LINKS"

hwnd_title = {}

def get_all_hwnd(hwnd, mouse):
    if(win32gui.IsWindow(hwnd) and
        win32gui.IsWindowEnabled(hwnd) and
        win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def find_win_by_title(title):
    win32gui.EnumWindows(get_all_hwnd,0)
    for h,t in hwnd_title.items():
        if t:
            if t==title:
                print(h,t)
                return h
                # left, top, right, bottom = win32gui.GetWindowRect(h)
                # print(left, top, right, bottom)

def print_all_win():
    win32gui.EnumWindows(get_all_hwnd,0)
    for h,t in hwnd_title.items():
        print(h,t)
