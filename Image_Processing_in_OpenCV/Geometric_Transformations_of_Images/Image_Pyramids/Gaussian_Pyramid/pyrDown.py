import cv2 as cv
img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg')
lower_reso = cv.pyrDown(img)
cv.imshow('2', img)
cv.imshow("1", lower_reso)
cv.waitKey(0)
cv.destroyAllWindows()