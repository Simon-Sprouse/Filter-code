#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:26:51 2023

@author: simonsprouse
"""

import colorsys


def bgrToHsv(color):
    
    b = int(color[0]/255)
    g = int(color[1]/255)
    r = int(color[2]/255)
    
    return colorsys.rgb_to_hsv(r, g, b)
    
    

def hsvToBgr(color):
    
    h, s, v = color
    
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    
    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    
    
    
    return [b, g, r]
    

    