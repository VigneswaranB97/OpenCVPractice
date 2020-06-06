# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:21:05 2020

@author: Vigneswaran B
"""

import cv2

image = cv2.imread('image.png')

print(image.shape)

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


corner = image[:100, :100]

cv2.imshow('Corner', corner)

cv2.waitKey(0)
cv2.destroyAllWindows()

(b, g, r) = image[0, 0]

# Blue Square on left top of Image
image[:100, :100] = (255, 0, 0) # Note [(B, G, R)]

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
