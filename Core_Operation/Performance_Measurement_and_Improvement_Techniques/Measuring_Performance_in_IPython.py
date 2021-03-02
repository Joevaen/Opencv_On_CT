import time
import cv2 as cv
import numpy as np

img = cv.imread(r'/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/9.jpg')
ts = time.time()
for i in range(1000000):
    z = cv.countNonZero(img[1,:,:])
te = time.time()
print(te - ts) # 0.6005682945251465

ts2 = time.time()
for i in range(1000000):
    z = np.count_nonzero(img[1,:,:])
te2 = time.time()
print(te2 - ts2) # 2.8813443183898926