import threading  # 导入threading库，用于线程管理
import time

import keyboard
import pyautogui
import pydirectinput

import imageToolkit
import shared
from shared import color_to_hsv


# 定义自动战斗类
class AutoFight:
    # 初始化
    def __init__(self):
        self.attacked = True  # 初始化受击状态标志
        self.running = False  # 初始化运行状态标志
        self.team = None  # 定义队伍变量
        self.width, self.height = None, None  # 定义屏幕宽高变量
        self.region = None  # 定义截图区域变量

    # 开始自动战斗
    def start(self, team):
        self.width, self.height = pyautogui.size()  # 获取屏幕宽高
        self.region = (0, 0, self.width, self.height)  # 定义截图区域
        self.running = True  # 设置运行状态
        self.attacked = False  # 设置受击状态
        self.team = team  # 获取当前队伍阵容
        if not self.running:
            shared.app.update_status("2秒后开始自动战斗")  # 更新状态信息
            time.sleep(2)  # 2秒后开始自动战斗
            # 创建自动战斗线程
            attack_thread = threading.Thread(target=self.auto_attack, args=(self.team,))
            defense_thread = threading.Thread(target=self.auto_defense, args=(self.team,))
            # 启动线程
            attack_thread.start()
            defense_thread.start()

    # 停止自动战斗
    def stop(self):
        if self.running:
            self.attacked = True  # 复位受击状态标志
            self.running = False  # 复位运行状态标志
            self.team.stop()  # 停止攻击

    # 自动攻击
    def auto_attack(self):
        while self.running:
            if keyboard.is_pressed("`"):  # 如果按下了`键，停止程序
                self.stop()
                break
            while self.attacked:
                self.team.fight()

    # 自动防御
    def auto_defense(self):
        while self.running:
            if keyboard.is_pressed("`"):  # 如果按下了`键，停止程序
                self.stop()
                break
            time.sleep(0.05)  # 增加截图间隔
            screenshot = pyautogui.screenshot(region=self.region)  # 截取屏幕
            hsv_img = imageToolkit.img2hsv(screenshot)  # 转为HSV格式
            # 遍历颜色和对应HSV范围
            for color, (lower_hsv, upper_hsv,) in color_to_hsv.items():
                contours = imageToolkit.get_contours(lower_hsv, upper_hsv, hsv_img)  # 根据HSV范围获取轮廓
                w_h_list = imageToolkit.get_rectangle_info(contours)  # 获取矩形信息
                if imageToolkit.check_contours(w_h_list):  # 检查轮廓，符合则进行防御
                    self.attacked = True  # 更新受击状态，停止攻击
                    self.team.stop()  # 停止攻击
                    self.perform_actions(color)  # 根据颜色执行相应的防御动作
                    time.sleep(0.3)  # 防御完后等待一段时间再攻击
                    self.attacked = False  # 更新受击状态，恢复攻击
                    break

    # 根据颜色执行相应的防御动作
    def perform_actions(self, color):
        if color == "yellow":  # 如果检测到黄色
            shared.app.update_status("黄色-即将格挡！")  # 更新状态信息
            pydirectinput.press("space")  # 按下space键
            time.sleep(1)  # 等待格挡反击
            pydirectinput.press("j")  # 再次按下j键
        elif color == "red":  # 如果检测到红色
            shared.app.update_status("红色-随即闪避")  # 更新状态信息
            pydirectinput.press("shift")  # 按下shift键
            time.sleep(0.2)  # 等待闪避反击
            pydirectinput.press("j")  # 再次按下j键
