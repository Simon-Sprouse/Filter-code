#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:26:51 2023

@author: simonsprouse
"""

import colorsys
from colr import color

def rgbToHsv(color):
    
    r = int(color[0]/255)
    g = int(color[1]/255)
    b = int(color[2]/255)
    
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    
    
    return [h, s, v]
    
    

def hsvToRgb(color):
    
    h, s, v = color
    
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    
    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    
    
    # print(r, g, b)
    
    
    return [r, g, b]








    
# n = 11

# for i in range(n):
    
#     hsv = rgbToHsv([255,0,0]) # red

#     inc = (1/(n-1))
#     hsv[0] += inc*i

#     end = hsvToRgb(hsv)
    
    
#     print(color("Hello", fore=[end[0], end[1], end[2]]))
    
    
    
    
    
    
    
    
def blend(color1, color2, n): 
    
    color1_hsv = rgbToHsv(color1)
    color2_hsv = rgbToHsv(color2)
    print(color1_hsv, color2_hsv)
    
    hue_gap = color2_hsv[0] - color1_hsv[0]
    print(hue_gap)
    
    hue_inc = (hue_gap/(n-1))
    print(hue_inc)
    
    for i in range(n):
        
        start = [0,0,0]
        start[0] = color1_hsv[0]
        start[1] = color1_hsv[1]
        start[2] = color1_hsv[2]
        

        start[0] += hue_inc*i

        end = hsvToRgb(start)
        
        
        print(color("Blend", fore=[end[0], end[1], end[2]]))
        
        
color1 = [255, 0, 0]
color2 = [255, 255, 0]
n = 11

blend(color1, color2, n)