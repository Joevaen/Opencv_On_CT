import numpy as np
import cv2 as cv
im = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[-1]
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(im,center,radius,(0,255,0),2)
cv.imshow('1', im)
cv.waitKey(0)