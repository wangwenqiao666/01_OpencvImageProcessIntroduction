# -*- coding: utf-8 -*-
import cv2
a=cv2.imread("image\\lenacolor.png")
b=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("lena",a)
cv2.imshow("gray",b)
cv2.waitKey()
cv2.destroyAllWindows()