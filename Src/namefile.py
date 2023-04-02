"""
Name File Code
by SIMON SPROUSE
(C) 2020
"""
import os.path

def fileName():
    
    print ("Save your original image in the same folder as this program.")
    
    filename_valid = False   
    while filename_valid == False:
        
        filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
        filename2 = filename + ".jpg"    
    
        if os.path.isfile(filename) == True:
            filename_valid = True
        elif os.path.isfile(filename2) == True:
            filename = filename2
            filename_valid = True
        else:
            print ("Something was wrong with that filename. Please try again.")
        
    print(filename)    
    return filename
    
