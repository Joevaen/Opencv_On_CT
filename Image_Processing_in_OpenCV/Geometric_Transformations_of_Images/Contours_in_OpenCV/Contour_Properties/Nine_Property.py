import numpy as np
import cv2 as cv
im = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[-1]

# Aspect Ratio 对象边界矩形的宽度与高度的比率
x,y,w,h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h

# Extent 轮廓面积与边界矩形面积之比
area = cv.contourArea(cnt)
x,y,w,h = cv.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area

# Solidity 坚固度是轮廓面积与其凸包面积的比率
area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area)/hull_area

# Equivalent Diameter 面积与轮廓面积相同的圆的直径
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

# Orientation 物体指向的角度。 以下方法还给出了主轴和副轴的长度
(x,y),(MA,ma),angle = cv.fitEllipse(cnt)

# Mask and Pixel Points 构成该对象的所有点
mask = np.zeros(img.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
# 下面这两个结果相同，但是方向不同
np_pixelpoints = np.transpose(np.nonzero(mask)) # numpy找mask所有点的api
cv_pixelpoints = cv.findNonZero(mask) # opencv找mask所有点的api

# Maximum Value, Minimum Value and their locations 最大值，最小值及其位置，我们可以使用遮罩图像找到这些参数
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img,mask = mask)

# Mean Color or Mean Intensity 平均颜色或平均强度
mean_val = cv.mean(im,mask = mask)

# Extreme Points 极端点是指对象的最顶部，最底部，最右侧和最左侧的点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])


