import cv2  # 导入OpenCV库，用于图像处理
import numpy as np  # 导入NumPy库，用于数值计算


def img2hsv(img):
    hsv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2HSV)
    return hsv_img


def get_contours(lower_hsv, upper_hsv, hsv_img):
    # 创建HSV范围掩码
    mask = cv2.inRange(hsv_img, lower_hsv, upper_hsv)
    # 使用形态学操作去除噪声
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # 查找外部轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # 返回轮廓列表
    return contours


def get_rectangle_info(contours):
    rectangle_info = []  # 存储矩形信息的列表
    for contour in contours:  # 遍历轮廓
        x, y, w, h = cv2.boundingRect(contour)  # 获取轮廓的最小外接矩形
        rectangle_info.append((w, h))  # 添加矩形信息到列表
    return rectangle_info


def check_contours(w_h_list):
    for w, h in w_h_list:
        # 检查矩形的宽和高是否符合指定条件
        if (w > 300 and h <= 30) or (w <= 30 and h > 300):
            return True  # 返回True表示找到了符合条件的轮廓
    return False  # 返回False表示未找到符合条件的轮廓
