import cv2 as cv
import numpy as np
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/thresh.jpg',0)
kernel = np.ones((9,9),np.uint8)
_tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow('tophat', _tophat)
cv.waitKey(0)
cv.destroyAllWindows()