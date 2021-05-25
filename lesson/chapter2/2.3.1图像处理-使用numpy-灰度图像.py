# -*- coding: utf-8 -*-
import cv2
import numpy as np
i=cv2.imread("image\lena256.bmp",cv2.IMREAD_UNCHANGED)

print(i.item(100,100))
i.itemset((100,100),255)
print(i.item(100,100))