# -*- coding: utf-8 -*-
import cv2
a=cv2.imread("image\\lenacolor.png")
rows,cols=a.shape[:2]
size=(round(cols*0.5),round(rows*1.5))
b=cv2.resize(a,size)
#注意：第2个参数控制的是“列长度、行长度”，注意顺序。
cv2.imshow("original",a)
cv2.imshow("resize",b)
cv2.waitKey()
cv2.destroyAllWindows()
