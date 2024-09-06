import shared
from character import *


# 队伍基类
class Team:
    def __init__(self):
        self.character = None  # 创建当前角色变量

    # 攻击方法
    def fight(self):
        pass

    # 停止攻击方法
    def stop(self):
        pass


# 莱卡恩-可琳-妮可 阵容
class LycaonCorinNicole(Team):
    def __init__(self):
        super().__init__()
        # 导入角色
        self.lycaon = Lycaon()
        self.corin = Corin()
        self.nicole = Nicole()
        shared.app.update_status("加载 莱卡恩-可琳-妮可 阵容")

    # 战斗方法
    def fight(self):

        self.character = "Lycaon"

        if self.character == "Lycaon":
            shared.app.update_status("当前角色：莱卡恩")
            self.lycaon.attack()

        if self.character == "Corin":
            shared.app.update_status("当前角色：可琳")

        if self.character == "Nicole":
            shared.app.update_status("当前角色：妮可")

    # 停止方法
    def stop(self):
        self.lycaon.stop_atk()
