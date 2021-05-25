# -*- coding: utf-8 -*-
import cv2
import numpy as np
a=cv2.imread("image\lenacolor.png")
rows,cols,chn=a.shape
b=cv2.split(a)[0]
g=np.zeros((rows,cols),a.dtype)
r=np.zeros((rows,cols),a.dtype)
m=cv2.merge([b,g,r])
cv2.imshow("merge",m)

cv2.waitKey()
cv2.destroyAllWindows()