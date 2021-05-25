# -*- coding: utf-8 -*-
import cv2
import numpy as np
i=cv2.imread("image\lenacolor.png",cv2.IMREAD_UNCHANGED)
'''
print(i.item(100,100,0))
i.itemset((100,100,0),255)
print(i.item(100,100,0))

print(i.item(100,100,1))
i.itemset((100,100,1),255)
print(i.item(100,100,1))
'''
print(i.item(100,100,2))
i.itemset((100,100,2),255)
print(i.item(100,100,2))