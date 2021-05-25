# -*- coding: utf-8 -*-
import cv2
import numpy as np
a=cv2.imread("image\lenacolor.png")
girl=cv2.imread("image\girl.bmp")
b=np.ones((101,101,3))
b=a[220:400,250:350]
girl[180:360,200:300]=b
cv2.imshow("original",girl)

cv2.waitKey()
cv2.destroyAllWindows()