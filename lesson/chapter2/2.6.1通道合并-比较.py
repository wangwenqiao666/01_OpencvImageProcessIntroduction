# -*- coding: utf-8 -*-
import cv2
import numpy as np
a=cv2.imread("image\lenacolor.png")
b,g,r=cv2.split(a)
cv2.imshow("original",a)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
m=cv2.merge([r,g,b])
cv2.imshow("merge",m)
cv2.waitKey()
cv2.destroyAllWindows()