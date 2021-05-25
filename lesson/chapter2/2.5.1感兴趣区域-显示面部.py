# -*- coding: utf-8 -*-
import cv2
import numpy as np
a=cv2.imread("image\lenacolor.png")
b=np.ones((101,101,3))
b=a[220:400,250:350]
cv2.imshow("original",a)
cv2.imshow("face",b)
cv2.waitKey()
cv2.destroyAllWindows()