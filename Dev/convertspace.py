#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:26:51 2023

@author: simonsprouse
"""

import colorsys
from colr import color

def bgrToHsv(color):
    
    b = int(color[0]/255)
    g = int(color[1]/255)
    r = int(color[2]/255)
    
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    
    
    return [h, s, v]
    
    

def hsvToBgr(color):
    
    h, s, v = color
    
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    
    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    
    
    
    return [b, g, r]


start = [0,0,255] #red

hsv = bgrToHsv(start)


hsv[0] += 0.2

end = hsvToBgr(hsv)


    


for i in range(11):
    
    hsv = bgrToHsv(start)


    hsv[0] += 0.1*i

    end = hsvToBgr(hsv)
    
    
    print(color("Hello", fore=[end[2], end[1], end[0]]))
    