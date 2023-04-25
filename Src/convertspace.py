#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:26:51 2023

@author: simonsprouse
"""

import colorsys
from colr import color

def rgbToHsv(color):
    
    r = float(color[0]/255)
    g = float(color[1]/255)
    b = float(color[2]/255)
    
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    
    
    return [h, s, v]
    
    

def hsvToRgb(color):
    
    h, s, v = color
    
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    
    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    
    
    return [r, g, b]



def rgbToBgr(arr):
    for i in arr: 
        temp = i[0]
        i[0] = i[2]
        i[2] = temp
    return arr


    
    
def blend(color1, color2, n): 
    
    output_list = []
    
    color1_hsv = rgbToHsv(color1)
    color2_hsv = rgbToHsv(color2)
    
    hue_gap = color2_hsv[0] - color1_hsv[0]
    hue_inc = (hue_gap/(n-1))
    
    sat_gap = color2_hsv[1] - color1_hsv[1]
    sat_inc = (sat_gap/(n-1))
    
    val_gap = color2_hsv[2] - color1_hsv[2]
    val_inc = (val_gap/(n-1))
    
    
    for i in range(n):
        
        start = [0,0,0]
        start[0] = color1_hsv[0]
        start[1] = color1_hsv[1]
        start[2] = color1_hsv[2]
        
        start[0] += hue_inc*i
        start[1] += sat_inc*i
        start[2] += val_inc*i
        
        end = hsvToRgb(start)
        
        # print(color("This text is demonstrating the blend function!", fore=[end[0], end[1], end[2]]))
        output_list.append(end)
        
    return output_list
        
color2 = [40, 120, 60]
color1 = [30, 40, 70]
n = 11

arr = blend(color1, color2, n)