import cv2 as cv
import numpy as np
import time

print(cv.useOptimized()) # True,默认开启
ts1 = time.time()
img1 = cv.imread(r'/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/9.jpg')
res1 = cv.medianBlur(img1,49)
te1 = time.time()
print(te1 - ts1)

cv.setUseOptimized(False)
print(cv.useOptimized())
ts2 = time.time()
img2 = cv.imread(r'/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/9.jpg')
res2 = cv.medianBlur(img2,49)
te2 = time.time()
print(te2 - ts2)


# True
# 0.014556407928466797
# False
# 0.014634370803833008
# 我这儿性能没提升呢？

