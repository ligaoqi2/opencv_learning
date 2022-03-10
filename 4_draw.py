# OpenCV教程_绘图功能
# OpenCV绘制不同的几何形状
"""
:params
  1. img:您要绘制形状的图像
  2. color:形状的颜色。对于BGR，将其作为元组传递，例如：(255,0,0)对于蓝色。对于灰度，只需传递标量值即可。
           厚度：线或圆等的粗细。如果对闭合图形（如圆）传递-1 ，它将填充形状。默认厚度= 1
  3. thickness:画线的粗细，必须使int型变量，-1表示填充颜色
  4. lineType:线的类型，是否为8连接线，抗锯齿线等。默认情况下，为8连接线。cv.LINE_AA给出了抗锯齿的线条，看起来非常适合曲线。
"""
# 画线
import numpy as np
import cv2 as cv
# 创建黑色的图像
img = np.zeros((512, 512, 3), np.uint8)
# Opencv可以绘制出所有以np.array为形式的图像
# 同理Opencv读图像读进来的也是np.array格式

# 绘制一条厚度为5的蓝色对角线
img = cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# cv.line(img, start_pt, end_pt, thickness, lineType)

# 绘制矩形
img = cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 2)
# cv.rectangle(img, leftOn_pt, downRight_pt, color, thickness)

# 绘制椭圆
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# cv.ellipse(img, 中心位置, (长轴长度，短轴长度), angle(椭圆沿逆时针旋转的角度), startAngle(沿主轴开始的角度), endAngle(沿主轴开始的角度), color, -1)

# 绘制多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))  # 将数组变为一列
# print("pts is {}".format(pts))
cv.polylines(img, [pts], True, (0, 255, 255))
# cv.polylines(img, list[points], boolean(False所画曲线不会闭合), color)

# 向图像添加文本
font = cv.FONT_HERSHEY_SIMPLEX  # 规定字体
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
# cv.putText(img, str(text), location, 字体, color, thickness, lineType)

# 绘制箭头
cv.arrowedLine(img, (100, 100), (200, 200), (0, 0, 255), 5)
# cv.arrowedLine(img, startPoint, endPoint, color, thickness)

# 绘制圆
frame = cv.circle(img, (300, 300), 20, (0, 0, 255), -1)
# cv.circle(img, 圆心(x, y), 半径, color, thickness)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
