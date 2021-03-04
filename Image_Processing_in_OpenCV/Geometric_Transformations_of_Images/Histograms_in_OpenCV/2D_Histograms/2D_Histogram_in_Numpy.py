import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
print(hsv[:,:,0].shape)
h = hsv[:,:,0]
s = hsv[:,:,1]
hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
cv.imshow('1', hist)
cv.waitKey(0)