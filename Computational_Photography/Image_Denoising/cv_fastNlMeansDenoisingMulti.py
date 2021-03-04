import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/qiao/PythonProjects/Opencv_On_CT/Test_Img/10.jpg', 0)
dst = cv.fastNlMeansDenoisingMulti(img, 2, 5, None, 4, 7, 35)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()