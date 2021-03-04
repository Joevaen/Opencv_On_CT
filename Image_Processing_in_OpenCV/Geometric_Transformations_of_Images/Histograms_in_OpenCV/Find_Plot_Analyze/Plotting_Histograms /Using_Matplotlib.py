import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/Test_Img/10.jpg')
# plt.hist(img.ravel(),256,[0,256])
# plt.show()

# 因为传入的图片只有一个通道有值，所以只能显示一个通道的
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()