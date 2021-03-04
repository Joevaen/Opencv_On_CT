import cv2 as cv
img = cv.imread('/Test_Img/10.jpg', 0)
hist = cv.calcHist([img],[0],None,[256],[0,256])
print(hist)