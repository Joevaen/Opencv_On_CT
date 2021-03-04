import numpy as np
import cv2 as cv
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
# cv.imwrite('clahe_2.jpg',cl1)
cv.imshow('2', img)
cv.imshow('1', cl1)
cv.waitKey(0)