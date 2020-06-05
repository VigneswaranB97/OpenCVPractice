# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:40:01 2020

@author: Vigneswaran B
"""

import cv2

videoCapture = cv2.VideoCapture('drop.avi') # Capture video from directory
fps = videoCapture.get(cv2.CAP_PROP_FPS) # Gets FPS

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)), 
        int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)))  # Gets size

videoWriter = cv2.VideoWriter('Output.avi', 
                              cv2.VideoWriter_fourcc('I', '4', '2', '0'), 
                              fps, 
                              size) # Writes or converts one format to another, (eg avi to mp4)


success, frame = videoCapture.read()

while success:  # Loop until there are no more frames
    videoWriter.write(frame)
    success, frame = videoCapture.read()
    
