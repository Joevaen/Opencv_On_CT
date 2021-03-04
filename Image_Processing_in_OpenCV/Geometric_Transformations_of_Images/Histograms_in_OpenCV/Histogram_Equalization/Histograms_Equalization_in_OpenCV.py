import numpy as np
import cv2 as cv

img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
# cv.imwrite('res.png',res)
cv.imshow('1', res)
cv.waitKey(0)