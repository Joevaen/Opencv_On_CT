import cv2 as cv
import numpy as np
img1 = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/9.jpg',0)
img2 = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
ret, thresh = cv.threshold(img1, 127, 255,0)
ret, thresh2 = cv.threshold(img2, 127, 255,0)
contours,hierarchy = cv.findContours(thresh,1,2)
cnt1 = contours[-1]
contours,hierarchy = cv.findContours(thresh2,1,2)
cnt2 = contours[-1]
ret = cv.matchShapes(cnt1,cnt2,1,0.0)
print( ret )