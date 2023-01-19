import win32gui

def print_all_active_window():
    res = dict()
    
    def find_active_hwnd(hwnd,position): 
        if(win32gui.IsWindow(hwnd) and
            win32gui.IsWindowEnabled(hwnd) and
            win32gui.IsWindowVisible(hwnd)):
            res.update({hwnd: win32gui.GetWindowText(hwnd)})
        
    win32gui.EnumWindows(find_active_hwnd,0)
    
    for h,t in res.items():
        print(h,t)

def find_window(className,windowTitle):
    hwnd = win32gui.FindWindow(className,windowTitle)
    return hwnd

def get_rect(hwnd):
    return win32gui.GetWindowRect(hwnd)
        
    
    
    
    
    