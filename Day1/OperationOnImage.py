# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:57:52 2020

@author: Vigneswaran B
"""

# Convert PNG to JPG or vise versa
import cv2
import numpy as np

# Reading and writing images

img = cv2.imread('random.jpg')
cv2.imwrite('random1.png', img)
imS = cv2.resize(img, (960, 540)) # Resize image
cv2.imshow('Image', imS) # Show image
cv2.waitKey(0) # Display the image infinitely until any keypress

# color to B/W image

bwImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('randomBW.png', bwImg)

# Image to Raw bytes

byteArray = bytearray(imS)
bgrImage = np.array(byteArray).reshape(960, 540, 3) 
cv2.imwrite('RandomGray.png', bgrImage)
