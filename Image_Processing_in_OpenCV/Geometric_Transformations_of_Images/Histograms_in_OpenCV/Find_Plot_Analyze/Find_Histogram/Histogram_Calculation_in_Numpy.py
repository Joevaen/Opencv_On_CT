import cv2 as cv
import numpy as np
img = cv.imread('/Test_Img/10.jpg', 0)
hist,bins = np.histogram(img.ravel(),256,[0,256])
print(hist)