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
import random
from convertspace import rgbToHsv, hsvToRgb, blend, rgbToBgr


### Enter filename ###
filename_valid = False
while filename_valid == False:
    path = input("Please enter a file name: ")
    if os.path.isfile(path) == True:
        filename_valid = True
    

### Handle file save ###
def saveFile(image_variable):
    file_name = input("Name your image: ")
    if ".png" not in file_name and ".jpg" not in file_name:
        file_name += ".jpg"
    cv2.imwrite(file_name, image_variable)
    print(file_name, "has been saved")
        
    


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
    


### Create Window ###
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.createTrackbar('Breakpoint', "Original Image", 0, 20, lambda x:None)



# Todo make this more efficient
def showVis(top_left, top_right, bottom_left, bottom_right):
    ''' Shows four images in a four image panel'''
    
    #create empty matrix
    vis = np.zeros((2*height, 2*width, channels), np.uint8)

    #combine 4 images
    vis[:height, :width, :channels] = top_left
    vis[:height, width:2*width, :channels] = top_right
    vis[height:2*height, :width, :channels] = bottom_left
    vis[height:2*height, width:2*width, :channels] = bottom_right

    cv2.imshow('Original Image', vis)



def makeColorList(n, method = "grey", shuffle = False):
    ''' Creates a color scheme list to match the breakpoints '''
    
    color_list = []
    
    if method == "grey":
        
        for i in range(n):
            r = random.randint(0,255)
            r = int(i*255/n)
            
            color_list.append([r, r, r])
        
    
    elif method == "rainbow": 
        
        inc = (1/(n))
        for i in range(n):
            
            hsv = rgbToHsv([255,0,255]) # red
            hsv[0] += inc*i
            end = hsvToRgb(hsv)
            
            color_list.append([end[2], end[1], end[0]])
            

    elif method == "blend":
        
        color2 = [40, 120, 60]
        color1 = [30, 40, 70]
        color_list = blend(color1, color2, n)
        
        color_list = rgbToBgr(color_list)
        
    elif method == "random":
        
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            
            x = random.randint(0,255)
            y = random.randint(0,255)
            z = random.randint(0,255)
            
            color2 = [a, b, c]
            color1 = [x, y, z]
            
            color_list = blend(color1, color2, n)
            color_list = rgbToBgr(color_list)
        


    if shuffle == True:
        random.shuffle(color_list)
        
    return color_list


### Initialize variables before loop ###
method = "rainbow"
compute = True
last_break = 0
customized_image = []



### Main loop ###
key_pressed = 69
while key_pressed != 27 and key_pressed != ord('s'):
    key_pressed = cv2.waitKey(300)
    
    shuffle = False
    
    ### Handle keypress ###
    if key_pressed == ord('r'):
        shuffle = True
        
    elif key_pressed == ord('1'):
        method = "rainbow"
        
    elif key_pressed == ord('2'):
        method = "blend"
        
    elif key_pressed == ord('3'):
        method = "random"
        
    elif key_pressed == ord('n'):
        
        if last_break + 1 <= 20:
            grayscale_break = cv2.setTrackbarPos('Breakpoint',"Original Image", last_break + 1)
    
    elif key_pressed == ord('b'):
        
        if last_break - 1 >= 0:
            grayscale_break = cv2.setTrackbarPos('Breakpoint',"Original Image", last_break - 1)
    
    if key_pressed == ord('s'):
        saveFile(customized_image)
        
    
    ### Retrieve trackbar info ###
    grayscale_break = cv2.getTrackbarPos('Breakpoint',"Original Image")
    number_of_splits = grayscale_break + 2

    
    if key_pressed != -1 or grayscale_break != last_break:
        compute = True
        
    last_break = grayscale_break


    
    
    
    ### Handle the computation
    if compute == True:
        
        compute = False

        """
        ---------------------
        Make the grayscale version
        ---------------------
        """
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
        
        
        breaks_image = cv2.bitwise_or(bins_list[0].color_image, bins_list[0].color_image)
    
        n = number_of_splits
        for i in range(1,n):
            breaks_image = cv2.bitwise_or(breaks_image, bins_list[i].color_image)
            
        """
        ---------------------
        Make the color version
        ---------------------
        """
    
        color_list = makeColorList(number_of_splits, method=method, shuffle=shuffle) 
            
          
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
            

    
        """
        ---------------------
        Display results
        ---------------------
        """
        showVis(original_image, grayscale_image, breaks_image, customized_image)
        
        

    
cv2.destroyAllWindows()
cv2.waitKey(10)

