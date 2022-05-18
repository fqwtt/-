import numpy as np
import cv2 as cv

# 读取图片并缩放
origin_img=cv.imread('img.png')
origin_img=cv.resize(origin_img,None,fx=1,fy=1)
rows,cols,channels=origin_img.shape

# 产生HSV图像用于二值化
HSV_img=cv.cvtColor(origin_img,cv.COLOR_BGR2HSV)

# 产生全0图像用于存放改变底色后的图像
img=np.zeros_like(origin_img)

# 定义滚动条的回调函数，此程序无需回调，所以Pass即可
def callback(x):
    pass

# 创建窗口
cv.namedWindow('window')
# 定义6个滚动条
lst1=['H low','S low','V low']
lst2=['H high','S high','V high']
for name in lst1+lst2:
    cv.createTrackbar(name, 'window', 0, 255, callback)

# 初始化参数
hsv_low=np.array([0,0,0])
hsv_high=np.array([0,0,0])
# 不断改变参数，显示改变后的图像
while True:
    for i in range(3):
        # 得到滑动条返回值，将其赋值给对应的参数
        hsv_low[i]=cv.getTrackbarPos(lst1[i],'window')
        hsv_high[i]=cv.getTrackbarPos(lst2[i],'window')

    # 二值化
    mask=cv.inRange(HSV_img, hsv_low, hsv_high)
    cv.imshow('mask',mask)
    img=origin_img.copy()

    # 改变底色,(0,0,255)为红色
    img[mask==255]=(0,0,255)
    cv.imshow('img_changed',img)

    # 按ESC退出
    if cv.waitKey(1)==27:
        break
cv.destroyAllWindows()