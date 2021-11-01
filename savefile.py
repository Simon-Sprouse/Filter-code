# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:43:58 2020

@author: Simon
THIS IS A SAVE FUNCTION
"""
import cv2

def saveFile(image_variable):
    file_name = input("Name your baby: ")
    if ".png" not in file_name and ".jpg" not in file_name:
        file_name += ".jpg"
    cv2.imwrite(file_name, image_variable)
    print(file_name, "has been saved")
    
