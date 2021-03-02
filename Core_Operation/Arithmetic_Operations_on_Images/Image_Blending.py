import cv2 as cv
import numpy as np

img1 = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/9.jpg')
img2 = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
img3 = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/11.jpg')
dst = cv.addWeighted(img1,0.3,img2,0.7,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()