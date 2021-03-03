import numpy as np
import cv2 as cv
im = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[-1]
cv.drawContours(im, [cnt], 0, (0,255,0), 3)  # 第三个参数是画第几个轮廓，-1表示所有轮廓
perimeter = cv.arcLength(cnt,True) # 第二个参数是确定是否是闭合曲线
cv.imshow('1', im)
cv.waitKey(0)
print(perimeter) # 拿到周长或者弧长