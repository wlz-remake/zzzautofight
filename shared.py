# 全局共享变量/对象

import numpy as np

# 窗口对象
app = None

# 黄光和红光的HSV范围
color_to_hsv = {
    "yellow": (np.array([20, 108, 236]), np.array([40, 235, 255])),  # 黄色的HSV范围
    "red": (np.array([0, 70, 240]), np.array([180, 160, 255])),  # 红色的HSV范围
}
