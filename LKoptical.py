import numpy as np
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='This sample demonstrates Lucas-Kanade Optical Flow calculation. \
                                              The example file can be downloaded from: \
                                              https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')
parser.add_argument('--image', '-i', type=str, help='path to image file')
args = parser.parse_args()
cap = cv.VideoCapture(args.image)
# 用于ShiTomasi拐点检测的参数
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)
# lucas kanade光流参数
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# criteria = (3, 10, 0.03)
# 学到了：函数传参可以通过字典指定键值对来传入，注意函数中引用要写为**lk_params

# 创建一些随机的颜色
color = np.random.randint(0, 255, (100, 3))
# 拍摄第一帧并在其中找到拐角
# 使用光流法必须先有特征点
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
# 创建用于作图的掩码图像
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 读到最后一帧再往后读
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 计算光流
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # print(p1)
    # print("p1's shape is {}".format(p1.shape))
    # print("st's shape is {}".format(st.shape))
    # print("err's shape is {}".format(err.shape))
    """
    nextPts,status,err = cv.calcOpticalFlowPyrLK( prevImg, nextImg, prevPts, nextPts[, status[, err[, winSize[, maxLevel[, criteria[, flags[, minEigThreshold]]]]]]])
    return:
        nextPtrs(np.array)(38, 1, 2):输出一个二维点的向量，这个向量可以是用来作为光流算法的输入特征点，也是光流算法在当前帧找到特征点的新位置（浮点数
        status(np.array)(38, 1):标志，在当前帧当中发现的特征点标志status==1，否则为0
        err(np.array)(38, 1):向量中的每个特征对应的错误率
    params:
        prevImg 上一帧图片
        nextImg:当前帧图片
        prevPts:上一帧找到的特征点向量
        nextPts:与返回值中的nextPtrs相同
        status:与返回的status相同
        err:与返回的err相同
        winSize:在计算局部连续运动的窗口尺寸（在图像金字塔中）
                图像金字塔：一幅图像经过逐级缩放后，将每一级在空间上搭起来
                特征点附近邻域取一个窗口，使得位移前后特征点邻域窗口内的像素进行差分后求平方，再求和，使得差异函数E(d)最小，即求得该点光流d(dx,dy)
        maxLevel:图像金字塔层数，0表示不使用金字塔
        criteria:寻找光流迭代终止的条件（在指定的最大迭代次数criteria.maxCount或搜索窗口移动小于criteria.epsilon时，迭代停止)
                 (3, 10, 0.03):10是最大迭代次数，0.03是窗口移动小于的大小
        flags:有两个宏，表示两种计算方法，分别是OPTFLOW_USE_INITIAL_FLOW表示使用估计值作为寻找到的初始光流，
                                          OPTFLOW_LK_GET_MIN_EIGENVALS表示使用最小特征值作为误差测量
        minEigThreshold:该算法计算光流方程的2×2规范化矩阵的最小特征值，除以窗口中的像素数; 
                        如果此值小于minEigThreshold，则会过滤掉相应的功能并且不会处理该光流，因此它允许删除坏点并获得性能提升。
    """
    # 选择良好点
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    # st == 1的索引给到p0和p1

    # 绘制跟踪
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        # ravel()方法将数组维度拉成一维数组
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        mask = cv.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv.circle(frame, (a, b), 5, color[i].tolist(), -1)
    img = cv.add(frame, mask)
    # cv2.add()两个图像进行相加：即将已经绘制光流线的图像与已经绘制特征点的图像相加
    cv.imshow('frame', img)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    # 没有上3行代码就无法进行视频的显示
    # 更新帧
    old_gray = frame_gray.copy()
    # 更新点
    p0 = good_new.reshape(-1, 1, 2)
