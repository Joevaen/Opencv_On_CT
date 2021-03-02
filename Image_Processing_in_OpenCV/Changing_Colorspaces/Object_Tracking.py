import cv2 as cv
import numpy as np

# 医学图像转换hsv以后，只有一个通道上值，其他两个通道都没有值，图像整体显示为灰色
img = cv.imread(r'/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
print(np.max(img[:,:,0]))
print(np.max(img[:,:,1]))
print(np.max(img[:,:,2]))
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
print(np.max(hsv[:,:,0]))
print(np.max(hsv[:,:,1]))
print(np.max(hsv[:,:,2]))
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
# # Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)
# # Bitwise-AND mask and original image
res = cv.bitwise_and(img,img, mask= mask)
cv.imshow('frame',img)
cv.imshow('mask',mask)
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()

