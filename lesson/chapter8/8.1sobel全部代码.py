# -*- coding: utf-8 -*-
import cv2
import numpy as np
o=cv2.imread('image\\lena.bmp',cv2.IMREAD_GRAYSCALE)
sobelx=cv2.Sobel(o,cv2.CV_64F,1,0)
sobely=cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx=cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely=cv2.convertScaleAbs(sobely)
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
sobelxy11=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy11 = cv2.convertScaleAbs(sobelxy11)
cv2.imshow("original",o)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("sobelxy",sobelxy)
cv2.imshow("sobelxy11",sobelxy11)
cv2.waitKey()
cv2.destroyAllWindows()