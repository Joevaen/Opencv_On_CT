import numpy as np
import cv2 as cv
im = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[-1]
hull = cv.convexHull(cnt)
_hull = cv.convexHull(cnt, returnPoints=False) # 得到hull中的点的索引
print(_hull) 
cv.drawContours(im, [cnt], 0, (0,255,0), 1)  # 第三个参数是画第几个轮廓，-1表示所有轮廓
cv.drawContours(im, [hull], 0, (255,255,0), 1)
cv.imshow('1', im)
cv.waitKey(0)