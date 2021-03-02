import cv2 as cv
import numpy as np

img = cv.imread(r'/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
b, g, r = cv.split(img)  # 把图像三个通道的二维数组分割开来
print(b, g, r)
print(img[:,:,0])
print(np.where((b == img[:,:,0]) == False))  # split的方法 == img[:,:,0]， 后者速度更快
