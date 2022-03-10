# OpenCV教程_图像入门
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 1.读取图像
img = cv2.imread("picture/1.png", 1)
print("format of img is {}".format(img.shape))
img2 = img[:, :, ::-1]
# [::-1]表示该维数组逆序
print("format of img is {}".format(img2.shape))
"""
第二个参数是一个标志，它指定了读取图像的方式。
0: 以灰度模式加载图像
1: 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
2: 加载图像，包括alpha通道(alpha透明度)
"""
# 2.显示图像
# cv2.imshow('image', img2)
# cv2.waitKey(0)
"""
cv.waitKey()是一个键盘绑定函数。其参数是以毫秒为单位的时间。
该函数等待任何键盘事件指定的毫秒。如果您在这段时间内按下任何键，程序将继续运行。
如果0被传递，它将无限期地等待一次敲击键。它也可以设置为检测特定的按键
它也可以设置为检测特定的按键，例如，如果按下键 a 等
"""
# cv2.destroyAllWindows()
"""
cv.destroyAllWindows()
只会破坏我们创建的所有窗口。如果要销毁任何特定的窗口，请使用函数 cv.destroyWindow()在其中传递确切的窗口名称作为参数。
"""
# 3.写入图像
k = cv2.waitKey(0) & 0xFF
# 64位计算机必须加上& 0xFF
if k == 27:         # 等待ESC退出
    cv2.destroyAllWindows()
elif k == ord('s'):
    # 等待关键字，保存和退出
    # ord()返回字符的ASCII码值
    cv2.imwrite('1_picture.png', img)
    cv2.destroyAllWindows()

# Matplotlib是Python的绘图库，提供多种绘图方法。
# OpenCV加载的彩色图像处于BGR模式。但是Matplotlib以RGB模式显示。因此，如果使用OpenCV读取彩色图像，则Matplotlib中将无法正确显示彩色图像
plt.imshow(img2, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()
