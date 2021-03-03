import cv2 as cv
import numpy as np
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/thresh.jpg',0)
kernel = np.ones((5,5),np.uint8)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('closing', closing)
cv.waitKey(0)
cv.destroyAllWindows()