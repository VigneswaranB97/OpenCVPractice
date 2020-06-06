# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:13:31 2020

@author: Vigneswaran B
"""


import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype='uint8')
canvas2 = np.zeros((300, 300, 3), dtype='uint8')

centerX, centerY = (canvas.shape[0] // 2, canvas.shape[1] // 2)

white = (255, 255, 255)

for i in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), i, white)  # Circles as Archery
    
cv2.imshow("Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
for i in range(25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    cent = np.random.randint(0, high=300, size=(2,))
    
    cv2.circle(canvas2, tuple(cent), radius, color, -1)   # 25 Random circles with random radius, centres and color
    
    
cv2.imshow("Image", canvas2)
cv2.waitKey(0)
cv2.destroyAllWindows()

