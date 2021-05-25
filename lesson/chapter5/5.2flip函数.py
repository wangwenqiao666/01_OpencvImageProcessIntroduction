# -*- coding: utf-8 -*-
import cv2
a=cv2.imread("image\\lenacolor.png")
# 上下翻转
b=cv2.flip(a,0)
cv2.imshow("original",a)
cv2.imshow("flip",b)
cv2.waitKey()
cv2.destroyAllWindows()

'''
# 左右翻转
b=cv2.flip(a,1)
cv2.imshow("original",a)
cv2.imshow("flip",b)
cv2.waitKey()
cv2.destroyAllWindows()
'''

'''
# 上下、左右方向同时翻转
b=cv2.flip(a,-1)
cv2.imshow("original",a)
cv2.imshow("flip",b)
cv2.waitKey()
cv2.destroyAllWindows()
'''