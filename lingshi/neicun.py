import win32gui as gui
import win32api as api
import win32con as con #control
import win32process as pro
import ctypes #呼叫C语言来帮忙

hwnd = gui.FindWindow(None,'ASTLIBRA Revision')

pid = pro.GetWindowThreadProcessId(hwnd)[1]

print(pid)

# 1.权限等级 2.操作是否影响其他程序 3.操作对象
caculate = api.OpenProcess(con.PROCESS_ALL_ACCESS,False,pid)
print(caculate)

# kernel32.dll 是操作内存的dll
k32 = ctypes.windll.LoadLibrary(r"C:\Windows\System32\kernel32.dll")

# 1. 操作对象 2.数据地址 3.要修改的值 4。数据类型
changeValue = ctypes.byref(ctypes.c_long(3000))

k32.WriteProcessMemory(int(caculate),0X01BC0BE4,changeValue,4)
# 计算机不识别py的数据操作内存，要修改的数据需要转换 py->C语言的数据->计算机能识别的实际
