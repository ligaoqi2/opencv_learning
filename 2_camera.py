# OpenCV教程_视频入门
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取摄像头采集的视频
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# TERMINATING ASYNC CALLBACK解决方案：cv2.VideoCapture(0, cv2.CAP_DSHOW)，不是cv2.VideoCapture(0)
# 创建一个 VideoCapture 对象。它的参数可以是设备索引或视频文件的名称。设备索引就是指定哪个摄像头的数字。
# 正常情况下，一个摄像头会被连接(就像我的情况一样)。所以我简单地传0(或-1)。你可以通过传递1来选择第二个相机，以此类推
# 在最后，不要忘记释放俘虏。
if not cap.isOpened():
    # 有时，cap可能尚未初始化捕获。在这种情况下，此代码显示错误。你可以通过cap.isOpened()方法检查它是否已初始化
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 我们在框架上的操作到这里
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示结果帧e
    cv2.imshow('frame', frame)
    # 此处只有显示没有保存视频
    if cv2.waitKey(1) == ord('q'):
        break
# 完成所有操作后，释放捕获器
cap.release()
cv2.destroyAllWindows()

# 可以使用cap.get(propId)方法访问该视频的某些功能，其中propId是0到18之间的一个数字。每个数字表示视频的属性
# 其中一些值可以使用cap.set(propId，value)进行修改。value是你想要的新值。
# 可以通过cap.get(cv.CAP_PROP_FRAME_WIDTH)和cap.get(cv.CAP_PROP_FRAME_HEIGHT)检查框架的宽度和高度
# cap.get(cv2.CAP_PROP_FPS)检查框架的帧率，帧率：一秒钟图像能刷新几次
# 默认情况下，它的分辨率为640x480。但我想将其修改为320x240。
# 只需使用和即可。ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)即可

