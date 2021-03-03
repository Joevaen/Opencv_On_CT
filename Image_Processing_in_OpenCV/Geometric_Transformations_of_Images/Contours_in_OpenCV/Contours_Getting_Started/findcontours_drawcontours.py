import numpy as np
import cv2 as cv
im = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(contours)
cv.drawContours(im, contours, -1, (0,255,0), 3)  # 第三个参数是画第几个轮廓，-1表示所有轮廓
cv.imshow('1', im)
cv.waitKey(0)
# cv.destroyAllWindows()
contours2, hierarchy2 = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(contours2)
cv.drawContours(im, contours2, -1, (0,255,0), 3)  # 第三个参数是画第几个轮廓，-1表示所有轮廓
cv.imshow('2', im)
cv.waitKey(0)
cv.destroyAllWindows()