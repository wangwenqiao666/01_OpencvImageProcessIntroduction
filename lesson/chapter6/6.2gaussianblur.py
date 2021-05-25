# -*- coding: utf-8 -*-
import cv2
o=cv2.imread("image\\lenaNoise.png")
print(o)
r=cv2.GaussianBlur(o,(3,3),0)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()