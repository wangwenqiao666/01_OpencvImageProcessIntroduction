# -*- coding: utf-8 -*-
import cv2
import numpy as np
a=cv2.imread("image\\lena256.bmp")
b=a
add1=a+b
add2=cv2.add(a,b)
cv2.imshow("original",a)
cv2.imshow("add1",add1)
cv2.imshow("add2",add2)
cv2.waitKey()
cv2.destroyAllWindows()