import threading
import time  # 导入time库，用于时间处理

import pydirectinput  # 导入pydirectinput库，用于直接模拟键盘输入

import shared


# 莱卡恩
class Lycaon:
    def __init__(self):
        self.atk_hit = 0
        self.lock = threading.Lock()  # 创建一个锁

    def stop_atk(self):
        with self.lock:
            self.atk_hit = 0

    def attack(self):
        with self.lock:
            self.atk_hit = 1
        while self.atk_hit:
            if self.atk_hit == 1:
                pydirectinput.keyDown("j")
                shared.app.update_status("莱卡恩一段")  # 更新状态信息
                time.sleep(0.5)  # 第一段蓄力时间
                pydirectinput.keyUp("j")
                time.sleep(0.5)  # 第一段后等待
                with self.lock:
                    self.atk_hit = 2
            if self.atk_hit == 2:
                pydirectinput.keyDown("j")
                shared.app.update_status("莱卡恩二段")  # 更新状态信息
                time.sleep(0.5)  # 第二段蓄力时间
                pydirectinput.keyUp("j")
                time.sleep(0.5)  # 第二段后等待
                with self.lock:
                    self.atk_hit = 3
            if self.atk_hit == 3:
                pydirectinput.keyDown("j")
                shared.app.update_status("莱卡恩三段")  # 更新状态信息
                time.sleep(0.5)  # 第三段蓄力时间
                pydirectinput.keyUp("j")
                time.sleep(1)  # 第三段后等待
                with self.lock:
                    self.atk_hit = 1


class Nicole:
    def __init__(self):
        pass


class Corin:
    def __init__(self):
        pass
