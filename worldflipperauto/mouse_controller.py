import pyautogui as auto


class MouseController:
    
    
    def move_left_click(postion):
        auto.moveTo(postion,duration=0.5)
        auto.click()
    
    @staticmethod
    def left_click():
        auto.click()