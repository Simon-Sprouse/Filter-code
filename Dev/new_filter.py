#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:27:12 2023

@author: simonsprouse
"""

### Here's my attempt at redoing my old highschool project

import os.path
import numpy as np
import cv2
import time

filename_valid = False

# while filename_valid == False:
#     path = input("Please enter a file name: ")
#     if os.path.isfile(path) == True:
#         filename_valid = True
    
### Todo: Remove
path = "img.jpeg"
    
original_image = cv2.imread(path, 1)
grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
grayscale_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)


height, width, channels = original_image.shape[:3]



cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)


# Todo make this more efficient
def showVis(top_left, top_right, bottom_left, bottom_right):
    
    #create empty matrix
    vis = np.zeros((2*height, 2*width, channels), np.uint8)

    #combine 4 images
    vis[:height, :width, :channels] = top_left
    vis[:height, width:2*width, :channels] = top_right
    vis[height:2*height, :width, :channels] = bottom_left
    vis[height:2*height, width:2*width, :channels] = bottom_right

    cv2.imshow('Original Image', vis)
    
    
    










key_pressed = 69
while key_pressed != 27:
    key_pressed = cv2.waitKey(10)
    
    
    
    red_paper = np.zeros((height,width,channels), np.uint8)
    yellow_paper = np.zeros((height,width,channels), np.uint8)
    
    red_paper[0:height,0:width, 0:channels] = (0,0,255)
    yellow_paper[0:height,0:width, 0:channels] = (0,255,255)
    
    showVis(original_image, grayscale_image, red_paper, yellow_paper)
    
    
cv2.destroyAllWindows()
cv2.waitKey(10)




