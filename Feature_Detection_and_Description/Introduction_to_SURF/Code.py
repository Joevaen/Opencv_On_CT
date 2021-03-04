import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg', 0)
surf = cv.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)
surf.setHessianThreshold(50000)
kp, des = surf.detectAndCompute(img,None)
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()