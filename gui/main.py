import getwindow
import pyautogui
import time
from imgmatching import *

# try:
#     but1 = pyautogui.locateCenterOnScreen('1.png')
#     butAdd = pyautogui.locateCenterOnScreen('+.png')
#     butEqule = pyautogui.locateCenterOnScreen('=.png')
#     print(but1,butAdd,butEqule)
    
    

#     pyautogui.moveTo(but1,duration=1)
#     pyautogui.click()

#     pyautogui.moveTo(butAdd,duration=1)
#     pyautogui.click()

#     pyautogui.moveTo(but1,duration=1)
#     pyautogui.click()

#     pyautogui.moveTo(butEqule,duration=1)
#     pyautogui.click()
# except KeyboardInterrupt:
#     print('取消')

#---
    
position = getwindow.find_win_by_title('183')
game = IsImage(position=position)
# 副本预计完成时间（秒）
predicted_time = 20
# 循环确认是否有铃铛的时间（秒）
ring_check_time = 1
# 循环确认是否完成副本的时间（秒）
complete_check_time = 10
# 副本名称
fuben_name = '人鱼公主超级'
# 副本图片
fuben_pic_path = 'pic/renyu.png'

while(True):
    time.sleep(ring_check_time)
    if(game.is_img('pic/ring3.png',0.8)):
        # 点击铃铛
        ring_pos = game.get_coor('pic/ring3.png',0.8)
        pyautogui.moveTo(ring_pos,duration=0.5)
        print('点击铃铛')
        pyautogui.click()
        # 判断有无超级风废龙
        time.sleep(1)
        if(game.is_img(fuben_pic_path, 0.9)):
            print('找到',fuben_name)
            pos =  game.get_coor(fuben_pic_path,0.9)
            pyautogui.moveTo(pos,duration=0.5)
            # 移动到参加按钮点击
            pyautogui.moveRel(300,0,duration=0.5)
            print('点击参加')
            pyautogui.click()
            while(True):
                time.sleep(2)
                # 点击准备
                if(game.is_img('pic/not_ready.png', 0.9)):
                    pos = game.get_coor('pic/not_ready.png', 0.9)
                    pyautogui.moveTo(pos,duration=0.5)
                    print('点击准备')
                    pyautogui.click()
                    # 等待时间和自动弹射时间
                    time.sleep(predicted_time)
                    # 判断是否完成
                    while(True):
                        print('开始检测是否完成')
                        time.sleep(complete_check_time)
                        if(game.is_img('pic/q_result.png', 0.8)):
                            print('完成，开始点击继续')
                            # 点击继续3次 ok(或者离开房间) 1次
                            count_continue = 0
                            count_ok = 0
                            while(count_continue<3 or count_ok<1):
                                time.sleep(1)
                                if(game.is_img('pic/continue.png', 0.9)):
                                    pos = game.get_coor('pic/continue.png', 0.9)
                                    pyautogui.moveTo(pos,duration=0.5)
                                    pyautogui.click()
                                    count_continue+=1
                                    print('点击继续,第',count_continue,'/3次')
                                if(game.is_img('pic/ok.png', 0.9)):
                                    pos = game.get_coor('pic/ok.png', 0.9)
                                    pyautogui.moveTo(pos,duration=0.5)
                                    pyautogui.click()
                                    count_ok+=1
                                    print('点击OK,第',count_ok,'/1次')
                                if(game.is_img('pic/leave.png', 0.9)):
                                    pos = game.get_coor('pic/leave.png', 0.9)
                                    pyautogui.moveTo(pos,duration=0.5)
                                    pyautogui.click()
                                    count_ok+=1
                                    print('点击离开房间,第',count_ok,'/1次')
                            break
                        # 副本通关失败
                        elif(game.is_img('pic/home.png', 0.8)):
                            print('副本通关失败,退出循环')
                            break
                    break
                # 进入失败:正在开始任务无法进入房间
                if(game.is_img('pic/cannotjoin_job_running.png', 0.9)):
                    pos = game.get_coor('pic/ok.png',0.9)
                    pyautogui.moveTo(pos,duration=0.5)
                    pyautogui.click()
                    break
                # 进入失败:房间已满员
                if(game.is_img('pic/cannotjoin_room_full.png', 0.9)):
                    pos = game.get_coor('pic/ok.png',0.9)
                    pyautogui.moveTo(pos,duration=0.5)
                    pyautogui.click()
                    break
        else:
            print('没有找到',fuben_name)
            pyautogui.click()
        
    
    


