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
grayscale_image_simple = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)


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
    
    
    
    grayscale_break = 100
    
    ### Set grayscale breaks
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break, grayscale_break, grayscale_break]
    min_grayscale_for_yellow =  [grayscale_break + 1, grayscale_break + 1, grayscale_break + 1]
    max_grayscale_for_yellow = [255, 255, 255]
    
    ### Create numpy arrays of grayscale breaks
    min_grayscale_for_red = np.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = np.array(max_grayscale_for_red, dtype = "uint8")
    min_grayscale_for_yellow = np.array(min_grayscale_for_yellow,
                                           dtype = "uint8")
    max_grayscale_for_yellow = np.array(max_grayscale_for_yellow,
                                           dtype = "uint8")
    
    ### Create masks for ranges
    block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_red,
                                              max_grayscale_for_red)
    block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_yellow,
                                                 max_grayscale_for_yellow)
    
    
    
    red_paper = np.zeros((height,width,channels), np.uint8)
    yellow_paper = np.zeros((height,width,channels), np.uint8)
    
    red_paper[0:height,0:width, 0:channels] = (0,0,255)
    yellow_paper[0:height,0:width, 0:channels] = (0,255,255)
    
    
    
    red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
                                           mask = block_all_but_the_yellow_parts)

    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)

    showVis(original_image, grayscale_image, customized_image, yellow_paper)
    
    
    
cv2.destroyAllWindows()
cv2.waitKey(10)




