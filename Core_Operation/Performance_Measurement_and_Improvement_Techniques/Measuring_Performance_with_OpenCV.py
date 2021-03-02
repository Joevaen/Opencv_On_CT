import cv2 as cv
import numpy as np

e1 = cv.getTickCount()
# your code execution
print("fuck u")
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
print(time)