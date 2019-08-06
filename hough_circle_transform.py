#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:48:19 2019

@author: rohit
"""

import cv2
import numpy as np


source_video='led1.mp4';save_img=source_video.split('.')[0]+'_save.jpg'

cap = cv2.VideoCapture(source_video)
if (cap.isOpened() == False):
   print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while(True):
    # Check if camera opened successfully
    if (cap.isOpened() == False): 
        print("Unable to read camera feed in loop !!! ")
        continue
    ret, img = cap.read()
    
    if ret == True:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img,5)
        #param1 : higher thresh of canny & lower = param1/2
        #param2 : accumalator thresh
        #min_dis=30, scale =1 
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,30,
                                    param1=70,param2=10,minRadius=5,maxRadius=10)
        
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            #cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        
    cv2.imshow('detected circles',img)
    k=cv2.waitKey(100)
    if k == 27:
        break
cv2.destroyAllWindows()