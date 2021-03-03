import numpy as np
import cv2 as cv
im = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[-1]

# 根据轮廓画方形框
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('1', im)
cv.waitKey(0)

# 最小面积矩形
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(im,[box],0,(0,0,255),2)
cv.imshow('2', im)
cv.waitKey(0)