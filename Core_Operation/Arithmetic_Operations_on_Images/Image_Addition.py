import cv2 as cv
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(type(x))

print(cv.add(x,y)) # cv是饱和运算
print(x+y) # np是模运算