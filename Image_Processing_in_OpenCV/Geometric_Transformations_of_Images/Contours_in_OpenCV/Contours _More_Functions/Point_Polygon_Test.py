import numpy as np
import cv2 as cv
im = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[-1]


# 测某点到轮廓的距离或者在不在轮廓内
dist = cv.pointPolygonTest(cnt,(0,0),True)
print(dist) # 在轮廓外距离为负值
# If you don't want to find the distance, make sure third argument is False,
# because, it is a time consuming process. So, making it False gives about 2-3X speedup.
dist = cv.pointPolygonTest(cnt,(0,0),False)
print(dist)