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




def makeBins(n):
    
    ### turn image array into 1dd sorted array
    flat = grayscale_image_simple.flatten()
    flat = np.sort(flat)
    print(len(flat))

    sorted_length = len(flat)

    
    bins = []
    for i in range(0,n):
        percentile = flat[int(i*sorted_length/n)]
        bins.append(percentile)

    bin_values = []
    for i in range(0,n-1):
        bin_value = flat[[(flat > bins[i]) & (flat < bins[i+1])]].mean()
        bin_values.append(bin_value)

    bin_value = flat[(flat > bins[n-1])].mean()
    bin_values.append(bin_value)
    
    
    return bins, bin_values
    

breaks, values = makeBins(2)


'''
n = 3
breaks: 0, 122, 179
values: 72, 160, 199
'''

def to3Channel(breaks, values):
    
    breaks_3channel = [[x,x,x] for x in breaks]
    values_3channel = [[x,x,x] for x in values]
    
    return breaks_3channel, values_3channel

breaks_3channel, values_3channel = to3Channel(breaks, values)

'''
n = 3
breaks: [0,0,0],[122,122,122],[179,179,179]
values: 7[72,72,72],[160,160,160],[199,199,199]
'''



    
    
    
    
    
class bin:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.color = [0,0,0] ### default to black
    
    def printBounds(self):
        print(self.lower, ",", self.upper)

    def setColor(self, color):
        self.color = color
        
    def createMask(self):
        
        self.lower = np.array(self.lower, dtype = "uint8")
        self.upper = np.array(self.upper, dtype = "uint8")
        
        self.mask = cv2.inRange(grayscale_image,self.lower, self.upper)

    def reColor(self):
        color_paper = np.zeros((height,width,channels), np.uint8)
        
        color_paper[0:height,0:width, 0:channels] = self.color
        
        self.color_image = cv2.bitwise_or(color_paper, color_paper,
                                            mask = self.mask)
        


break_list = breaks_3channel

def makeBinsList(n):

    bin_list = []
    bin_list.append(bin(break_list[0],break_list[1]))

    for i in range(1,n-1):
        bin_list.append(bin([x+1 for x in break_list[i]],break_list[i+1]))
    
    bin_list.append(bin(break_list[n-1],[255,255,255]))
    
        
    return bin_list
    

bins_list = makeBinsList(2)

for x, i in enumerate(bins_list):
    print(x)
    i.setColor(values_3channel[x])


for i in bins_list:
    i.createMask()
    

for i in bins_list:
    i.reColor()



for i in bins_list:
    i.printBounds()
    








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
    
    
    


    customized_image = cv2.bitwise_or(bins_list[0].color_image, bins_list[1].color_image)

    showVis(original_image, grayscale_image, customized_image, customized_image)
    
    
    
cv2.destroyAllWindows()
cv2.waitKey(10)




