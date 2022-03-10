# OpenCV教程_视频入门
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 读取文件视频
cap = cv.VideoCapture('video/01153.mp4')
# python 读指定路径的文件必须使用反斜杠/或者在路径前面加\r取消路径中的转义字符
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
count = cap.get(cv.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv.CAP_PROP_FPS)

# 保存视频
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('video/output.mp4', fourcc, fps, (width, height))
# 创建一个 VideoWriter 对象。我们应该指定输出文件名
# 指定 FourCC 代码。然后传递帧率的数量和帧大小
# FourCC用于指定视频编解码器的4字节代码,一般采用*mp4v
while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        # 此句话会输出,因为读到最后一帧再读一帧就读不到了
        break
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    # cv.imshow()直接展示了每一帧，所以帧率会有变化
    out.write(frame)
    # 将帧写入视频文件
    if cv.waitKey(1) == ord('q'):
        break
    """
    if cv.waitKey(1) == number:
    break
    上面两句必须要有,否则无法进行实时的显示
    """
print("视频总帧数为{}".format(count))
cap.release()
out.release()
cv.destroyAllWindows()

