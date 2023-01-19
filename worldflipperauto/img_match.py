"""
使用opencv进行模板匹配即目标图片识别
定义两种主要方法
    1.匹配到目标图片后返回图片坐标
    2.检测当前屏幕下是否出现目标图片
封装成类可以随时调用
需要安装第三方库
    pycharm安装opencv
    控制台pip install pyautogui
    pycharm安装numpy
    控制台pip install pynput
"""
import time
import cv2
import pyautogui
import numpy as np


class IsImage:
    def __init__(self, target=None, value=None,position=None):
        self.target = target
        self.value = value
        self.position = position
        self.image = "truncate_img.jpg"

    @staticmethod
    def get_img(position):
        """
        截取窗口屏幕
        :return: 保存窗口图片
        """
        left, top, right, bottom = position
        img = pyautogui.screenshot(region=(left,top, right-left, bottom-top))
        img.save('truncate_img.jpg')
        return img

    def get_coor(self, target, value):
        """
        找到目标图片返回图片当前坐标
        :param target:目标图片 类型:str
        :param value:相似度阈值 类型:float
        :return:图片当前坐标
        """
        self.get_img(self.position)
        img_rgb = cv2.imread(self.image)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(target, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = value
        loc = np.where(res >= threshold)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        left_top = max_loc  # 左上角
        right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
        coordinates = (
            (left_top[0] + ((right_bottom[0] - left_top[0]) / 2)),
            (left_top[1] + ((right_bottom[1] - left_top[1]) / 2)))
        if len(loc[0]) > 0:
            # 找到目标图片返回图片当前坐标
            return coordinates

    def is_img(self, target, value):
        """
        检测有没有目标图片
        :param target: 目标图片 类型:str
        :param value: 相似度阈值 类型:float
        :return: True or False
        """
        self.get_img(self.position)
        img_rgb = cv2.imread(self.image)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(target, 0)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = value
        loc = np.where(res >= threshold)
        if len(loc[0]) > 0:
            # 找到目标图片返回真
            return True


if __name__ == '__main__':
    test = IsImage()

    # data = test.get_coor("target.jpg", 0.9)
    # time.sleep(2)
    # test.click(data)

    if test.is_img("111.jpg", 0.9):
        print("找到了")
    else:
        print("没找到")
