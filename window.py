import tkinter as tk  # 导入tkinter库，用于创建GUI

from autoFight import AutoFight
from team import *


class Window:
    def __init__(self):
        self.autoFight = AutoFight()  # 实例化自动战斗类

        self.root = tk.Tk()  # 创建Tkinter根窗口

        self.root.title("红黄光检测")  # 设置窗口标题

        self.root.geometry("300x400")  # 设置窗口大小

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # 添加关闭事件处理

        self.start_button = tk.Button(self.root, text="开始", command=self.start)  # 创建开始按钮
        self.start_button.pack(pady=5)  # 显示开始按钮并设置间距

        self.stop_button = tk.Button(self.root, text="停止", command=self.stop)  # 创建停止按钮
        self.stop_button.pack(pady=5)  # 显示停止按钮并设置间距

        self.status_label = tk.Label(self.root, text="状态：关闭", bg="red", fg="white")  # 创建状态标签
        self.status_label.pack(pady=5)  # 显示状态标签并设置间距

        self.log_text = tk.Text(self.root, height=10, state="disabled")  # 创建用于显示日志的文本框
        self.log_text.pack(pady=10, fill="both", expand=True)  # 显示日志文本框并设置填充和扩展

        # 窗口置顶复选框
        self.topmost_var = tk.IntVar()  # 创建整型变量用于窗口置顶选择
        self.topmost_check = tk.Checkbutton(self.root, text="窗口置顶", variable=self.topmost_var, command=self.set_topmost)  # 创建窗口置顶复选框
        self.topmost_check.pack(pady=5, anchor="ne")  # 显示窗口置顶复选框并设置间距和位置

        self.root.mainloop()  # 运行Tkinter主循环

    def start(self):
        self.status_label.config(text="状态：开启", bg="green")  # 更新状态标签为开启
        team = LycaonCorinNicole()  # 设置队伍阵容
        self.autoFight.start(team)

    def stop(self):
        self.status_label.config(text="状态：关闭", bg="red")  # 更新状态标签为关闭
        self.autoFight.stop()

    def update_status(self, text):
        # 更新日志窗口
        self.log_text.config(state="normal")  # 设置文本框为可编辑状态
        self.log_text.insert("end", text + "\n")  # 在文本框末尾插入新日志
        self.log_text.see("end")  # 滚动到文本框末尾
        self.log_text.config(state="disabled")  # 设置文本框为不可编辑状态

    def set_topmost(self):
        # 设置窗口置顶
        self.root.attributes(
            "-topmost", self.topmost_var.get()
        )  # 根据复选框状态设置窗口置顶属性

    def on_closing(self):
        # 当窗口被关闭时调用此方法
        print("等待线程结束")
        self.stop()
        self.root.destroy()
