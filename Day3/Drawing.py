# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:59:05 2020

@author: Vigneswaran B
"""


import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype='uint8') # Unsigned 8 bit integer

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green) # a Line

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)

cv2.rectangle(canvas, (10, 10), (30, 30), green) # a Rectangle

blue = (255, 0, 0)
cv2.rectangle(canvas, (50, 10), (70, 40), blue, -1) # -1 is for filled in rectangle

cv2.rectangle(canvas, (20, 30), (40, 50), red, 3) # 3 is thickness for rectangle

cv2.imshow("Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

