import cv2 as cv
import numpy as np

a = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
print(a)

b = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
print(b)

c = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
print(c)

img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/thresh.jpg',0)
# kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img,a,iterations = 1)
dilation2 = cv.dilate(img,b,iterations = 1)
dilation3 = cv.dilate(img,c,iterations = 1)
cv.imshow('dilation', dilation)
cv.imshow('dilation2', dilation2)
cv.imshow('dilation3', dilation3)
cv.waitKey(0)
cv.destroyAllWindows()