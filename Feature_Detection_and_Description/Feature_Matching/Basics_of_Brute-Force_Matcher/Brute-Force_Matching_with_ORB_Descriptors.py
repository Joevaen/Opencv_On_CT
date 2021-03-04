import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1 = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg',cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/9.jpg',cv.IMREAD_GRAYSCALE) # trainImage
# print(type(img2[0][0]))
# img2 = img2[100:200, 100:200]
# print(type(img2[0][0]))
# # Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()