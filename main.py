import ctypes  # 导入ctypes库，用于调用系统函数
import sys  # 导入sys库，用于系统相关操作

import shared
from window import Window


# 定义函数以检查是否以管理员权限运行
def is_admin():
    try:
        # 调用IsUserAnAdmin函数检查是否为管理员
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        # 如果出现异常，则返回False
        return False


if __name__ == "__main__":
    if is_admin():  # 如果以管理员权限运行
        shared.app = Window()  # 创建应用程序实例


    else:
        # 以管理员权限重新启动脚本
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )  # 以管理员权限重新启动脚本
