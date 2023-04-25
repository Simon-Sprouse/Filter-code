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
import random
from convertspace import rgbToHsv, hsvToRgb

red = [0,0,255]
print(rgbToHsv(red))


filename_valid = False

# while filename_valid == False:
#     path = input("Please enter a file name: ")
#     if os.path.isfile(path) == True:
#         filename_valid = True
    
### Todo: Remove
path = "img7.jpeg"


    


### Read in the image from the file path ### 
original_image = cv2.imread(path, 1)
grayscale_image_simple = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

height, width, channels = original_image.shape[:3]




def makeBins(n):
    ''' Finds pixel values which divide array into n equal subarrays '''
    
    ### turn image array into 1d sorted array ###
    flat = grayscale_image_simple.flatten()
    flat = np.sort(flat)
    sorted_length = len(flat)

    ### bins here means breaks in pixle values ###
    bins = []
    for i in range(0,n):
        percentile = flat[int(i*sorted_length/n)]
        bins.append(percentile)

    ### find the represenative color for each bin ###
    bin_values = []
    for i in range(0,n-1):
        bin_value = flat[[(flat > bins[i]) & (flat < bins[i+1])]].mean()
        bin_values.append(bin_value)
    bin_value = flat[(flat > bins[n-1])].mean()
    bin_values.append(bin_value)
    
    
    return bins, bin_values
    

def to3Channel(breaks, values):
    ''' Takes a 1 channel grayscale value and converts to 3 channel BGR value '''
    
    breaks_3channel = [[x,x,x] for x in breaks]
    values_3channel = [[x,x,x] for x in values]
    
    return breaks_3channel, values_3channel 


'''
This bin class represents the actual bin of pixels
self.lower is the lower bound for pixel values
self.upper is the upper bound for pixel values
self.color is the color which will be used to represent the bin
'''
class bin:
    
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.color = [155,0,0] ### default to blue
    
    def printBounds(self):
        print(self.lower, ",", self.upper)

    def setColor(self, color):
        self.color = color
        
    def createMask(self):
        ''' Creates a cv2 mask for the bin '''
        
        ### Cast into type uint8 ###
        self.lower = np.array(self.lower, dtype = "uint8")
        self.upper = np.array(self.upper, dtype = "uint8")
        
        ### Create cv2 mask ###
        self.mask = cv2.inRange(grayscale_image,self.lower, self.upper)

    def reColor(self):
        ''' Recolor the mask to self.color '''
        
        color_paper = np.zeros((height,width,channels), np.uint8) ### make size
        color_paper[0:height,0:width, 0:channels] = self.color    ### recolor
        self.color_image = cv2.bitwise_or(color_paper, color_paper,
                                            mask = self.mask)
        

def makeBinsList(n, break_list):
    ''' Makes a list of bin objects '''
    
    bin_list = []
    bin_list.append(bin(break_list[0],break_list[1]))
    for i in range(1,n-1):
        bin_list.append(bin([x+1 for x in break_list[i]],break_list[i+1]))
    bin_list.append(bin(break_list[n-1],[255,255,255]))
    
        
    return bin_list
    



    


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



def makeColorList(n, method = "grey"):
    
    color_list = []
    
    if method == "grey":
        
        for i in range(n):
            r = random.randint(0,255)
            r = int(i*255/n)
            
            color_list.append([r, r, r])
        
        return color_list
    
    if method == "rainbow": 
        
        inc = (0.4/(n-1))
        for i in range(n):
            
            hsv = rgbToHsv([255,0,255]) # red

            hsv[0] += inc*i

            end = hsvToRgb(hsv)
            
            
            color_list.append([end[2], end[1], end[0]])
            
        return color_list
    
    if method == "random":
        
        inc = (0.2/(n-1))
        for i in range(n):
            
            hsv = rgbToHsv([255,0,0]) # red

            hsv[0] += inc*i

            end = hsvToRgb(hsv)
            
            
            color_list.append([end[2], end[1], end[0]])
            
            random.shuffle(color_list)
            
        return color_list
        
    
    
    
    else:
        
        return []




i = 0

key_pressed = 69
while key_pressed != 27:
    key_pressed = cv2.waitKey(3000)
    
    number_of_splits = 2 + i
    i += 1
    breaks, values = makeBins(number_of_splits)
    breaks_3channel, values_3channel = to3Channel(breaks, values)
    bins_list = makeBinsList(number_of_splits, breaks_3channel)
    
    grey_list = makeColorList(number_of_splits) 
    
    
    for x, i in enumerate(bins_list):
        i.setColor(grey_list[x])
    
    for i in bins_list:
        i.createMask()
        
    for i in bins_list:
        i.reColor()
    
    
    # for i in bins_list:
    #     i.printBounds()
        


    breaks_image = cv2.bitwise_or(bins_list[0].color_image, bins_list[0].color_image)


    n = number_of_splits
    for i in range(1,n):
        breaks_image = cv2.bitwise_or(breaks_image, bins_list[i].color_image)
        
        
        
        
        
        
        
    color_list = makeColorList(number_of_splits, method="rainbow") 
        
      
    for x, i in enumerate(bins_list):
        i.setColor(color_list[x])
    
    for i in bins_list:
        i.createMask()
        
    for i in bins_list:
        i.reColor()
    


    customized_image = cv2.bitwise_or(bins_list[0].color_image, bins_list[0].color_image)

    n = number_of_splits
    for i in range(1,n):
        customized_image = cv2.bitwise_or(customized_image, bins_list[i].color_image)
        
    



    showVis(original_image, grayscale_image, breaks_image, customized_image)
    
    
    
cv2.destroyAllWindows()
cv2.waitKey(10)

