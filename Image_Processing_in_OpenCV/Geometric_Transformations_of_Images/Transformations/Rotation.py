import cv2 as cv
import numpy as np

img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg', 0)
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()