""" 
FINAL FILTER CODE
Kyle Fricke and Cheryl Farmer, Engineer Your World

Modified by SIMON SPROUSE
(C) 2020
"""

import cv2
import numpy
import savefile
import namefile
import random
from colr import color

#filenameInput
filename = namefile.fileName()

#grayscale image creation
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#dimensions for grayscale images
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#declare color paper variables
red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
yellow_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
green_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
cyan_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
blue_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
purple_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)


#declare windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Customized Image2')
cv2.namedWindow('Customized Image3')
cv2.namedWindow('Test Image')
cv2.namedWindow('Trackbar')

cv2.resizeWindow('Trackbar',700,700)

#display images
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)

#create trackbars
cv2.createTrackbar('Grayscale', 'Trackbar', 0, 255, lambda x:None)
cv2.createTrackbar('Grayscale2', 'Trackbar', 0, 255, lambda x:None)
cv2.createTrackbar('Grayscale3', 'Trackbar', 0, 255, lambda x:None)
cv2.createTrackbar('Grayscale4', 'Trackbar', 0, 255, lambda x:None)
cv2.createTrackbar('Grayscale5', 'Trackbar', 0, 255, lambda x:None)
cv2.createTrackbar('Color', 'Trackbar', 0, 1535, lambda x:None)
cv2.createTrackbar('Color2', 'Trackbar', 0, 1535, lambda x:None)
cv2.createTrackbar('Color3', 'Trackbar', 0, 1535, lambda x:None)
cv2.createTrackbar('Color4', 'Trackbar', 0, 1535, lambda x:None)
cv2.createTrackbar('Color5', 'Trackbar', 0, 1535, lambda x:None)
cv2.createTrackbar('Color6', 'Trackbar', 0, 1535, lambda x:None)
cv2.createTrackbar('Hue', 'Trackbar', 0, 510, lambda x:None)
cv2.createTrackbar('Hue2', 'Trackbar', 0, 510, lambda x:None)
cv2.createTrackbar('Hue3', 'Trackbar', 0, 510, lambda x:None)
cv2.createTrackbar('Hue4', 'Trackbar', 0, 510, lambda x:None)
cv2.createTrackbar('Hue5', 'Trackbar', 0, 510, lambda x:None)
cv2.createTrackbar('Hue6', 'Trackbar', 0, 510, lambda x:None)
cv2.createTrackbar('Joke', 'Trackbar', 0, 3000, lambda x:None)

#these lists set the trackbar position/color
def preset():
    
        cv2.setTrackbarPos('Grayscale', 'Trackbar', grayscale_list[0])
        cv2.setTrackbarPos('Grayscale2', 'Trackbar', grayscale_list[1])
        cv2.setTrackbarPos('Grayscale3', 'Trackbar', grayscale_list[2])
        cv2.setTrackbarPos('Grayscale4', 'Trackbar', grayscale_list[3])
        cv2.setTrackbarPos('Grayscale5', 'Trackbar', grayscale_list[4])
    
        cv2.setTrackbarPos('Color','Trackbar',preset_list[0])
        cv2.setTrackbarPos('Color2','Trackbar',preset_list[1])
        cv2.setTrackbarPos('Color3','Trackbar',preset_list[2])
        cv2.setTrackbarPos('Color4','Trackbar',preset_list[3])
        cv2.setTrackbarPos('Color5','Trackbar',preset_list[4])
        cv2.setTrackbarPos('Color6','Trackbar',preset_list[5])
        
        cv2.setTrackbarPos('Hue', 'Trackbar', hue_list[0])
        cv2.setTrackbarPos('Hue2', 'Trackbar', hue_list[1])
        cv2.setTrackbarPos('Hue3', 'Trackbar', hue_list[2])
        cv2.setTrackbarPos('Hue4', 'Trackbar', hue_list[3])
        cv2.setTrackbarPos('Hue5', 'Trackbar', hue_list[4])
        cv2.setTrackbarPos('Hue6', 'Trackbar', hue_list[5])
        
''' 
This is the FUNKY math that puts the rbg spectrum on one slider
The track argument will measure the trackbar position and determine the color range
The hue argument moves the colors either towards white or black
'''

def funkyMath(track,hue):
    
    if track <= 0:
        red = 0 
        green = 0
        blue = 0        
    elif track > 0 and track <= 255 and hue <= 255:
        red = (hue*255)/255 #255
        green = (hue*track)/255 #track
        blue = 0 #0       
    elif track > 0 and track <= 255 and hue > 255:
        red = 255 #255
        green = track + (hue-255)*(255-track)/(255) #track
        blue = (hue-255) #0 
    elif track > 255 and track <= 511 and hue <= 255:
        red = (hue*(511-track))/255
        green = (hue*255)/255
        blue = 0        
    elif track > 255 and track <= 511 and hue > 255:
        red = (511-track) + (hue-255)*(255-(511-track))/(255)
        green = 255
        blue = (hue-255)
    elif track > 511 and track <= 767 and hue <= 255:
        red = 0
        green = (hue*255)/255
        blue = (hue*(track-511))/255       
    elif track > 511 and track <= 767 and hue > 255:
        red = (hue-255)
        green = 255
        blue = (track-511) + (hue-255)*(255-(track-511))/(255)   
    elif track > 767 and track <= 1023 and hue <= 255:
        red = 0
        green = (hue*(1023-track))/255
        blue = (hue*255)/255       
    elif track > 767 and track <= 1023 and hue > 255:
        red = (hue-255)
        green = (1023-track) + (hue-255)*(255-(1023-track))/(255)
        blue = 255     
    elif track > 1023 and track <= 1279 and hue <= 255:
        red = (hue*(track-1023))/255
        green = 0
        blue = (hue*255)/255      
    elif track > 1023 and track <= 1279 and hue > 255:
        red = (track-1023) + (hue-255)*(255-(track-1023))/(255)
        green = (hue-255)
        blue = 255      
    elif track > 1279 and track < 1535 and hue <= 255:
        red = (hue*255)/255
        green = 0
        blue = (hue*(1535-track))/255       
    elif track > 1279 and track < 1535 and hue > 255:
        red = 255
        green = (hue-255)
        blue = (1535-track) + (hue-255)*(255-(1535-track))/(255)     
    elif track == 1535:
        red = (hue*255)/255
        green = (hue*255)/255
        blue = (hue*255)/255
        
    red = round(red)    
    green = round(green)    
    blue = round(blue)    

    return blue, green, red


#random stuff to make the while loop function
keypressed = 69
preset_list = [1,250,510,760,1020,1280]
hue_list = [255,255,255,255,255,255]
grayscale_list = [1,1,1,1,1]
preset()


#loop for image creation
while keypressed != 27:
    
    keypressed = cv2.waitKey(1)
    
    #variables for trackbar position
    x = cv2.getTrackbarPos('Color','Trackbar')
    y = cv2.getTrackbarPos('Color2','Trackbar')
    z = cv2.getTrackbarPos('Color3','Trackbar')
    a = cv2.getTrackbarPos('Color4','Trackbar')
    b = cv2.getTrackbarPos('Color5','Trackbar')
    c = cv2.getTrackbarPos('Color6','Trackbar')  
    h0 = cv2.getTrackbarPos('Hue','Trackbar')
    h1 = cv2.getTrackbarPos('Hue2','Trackbar')
    h2 = cv2.getTrackbarPos('Hue3','Trackbar')
    h3 = cv2.getTrackbarPos('Hue4','Trackbar')
    h4 = cv2.getTrackbarPos('Hue5','Trackbar')
    h5 = cv2.getTrackbarPos('Hue6','Trackbar')
    grayscale_break = cv2.getTrackbarPos('Grayscale','Trackbar')
    grayscale_break2 = cv2.getTrackbarPos('Grayscale2','Trackbar')
    grayscale_break3 = cv2.getTrackbarPos('Grayscale3','Trackbar')
    grayscale_break4 = cv2.getTrackbarPos('Grayscale4','Trackbar')
    grayscale_break5 = cv2.getTrackbarPos('Grayscale5','Trackbar')
    
    grayscale_list = [grayscale_break,grayscale_break2,grayscale_break3,grayscale_break4,grayscale_break5]

    
    """
    This next set of arguments creates presets. The trackbar values are set to
    specific colors and are refreshed at the new locations.
    The = key goes back to default colors.
    1-9 Are presets.  The keys: [, ], `, and - shuffle the colors.
    """
    
    if keypressed == ord('1'):
        
        preset_list = [1,127,159,243,1534,1249]
        hue_list = [255,255,255,255,255,255]
        preset()
        
    elif keypressed == ord('2'):
        
        preset_list = [688,826,900,1027,1154,1285]
        hue_list = [255,255,255,255,255,255]
        preset()
        
    elif keypressed == ord('3'):
        
        preset_list = [1335,1335,1200,1200,1130,1130]
        hue_list = [420,340,250,190,144,60]
        preset()
        
    elif keypressed == ord('4'):
        
        preset_list = [711,720,850,1250,1175,1535]
        hue_list = [420,255,255,255,255,255]
        preset()
        
    elif keypressed == ord('5'):
        
        preset_list = [511,511,511,511,511,511]
        hue_list = [69,113,144,190,243,415]
        preset()
        
    elif keypressed == ord('6'):
        
        preset_list = [1000,1016,1217,1,1,1535]
        hue_list = [63,255,255,255,341,255]
        preset()
        
    elif keypressed == ord('7'):
        
        preset_list = [1535,286,11,127,159,0]
        hue_list = [255,255,255,255,255,255]
        preset()
        
    elif keypressed == ord('8'):
        
        preset_list = [0,1535,0,1535,0,1535]
        hue_list = [255,255,255,255,255,255]
        preset()
    
    elif keypressed == ord('9'):
        
        preset_list = [1535,1535,1535,1535,1535,1535]
        hue_list = [0,51,102,153,204,255]
        preset()
    
    elif keypressed == ord('0'):
        preset_list = [1535-x,1535-y,1535-z,1535-a,1535-b,1535-c,]    
        preset()
   
    elif keypressed == ord('='):
        
        preset_list = [1,250,510,760,1020,1280]
        hue_list = [255,255,255,255,255,255]
        preset()
        
    #This is the perfect setting for the fence image :)    
    elif keypressed == ord('f'):
        grayscale_list = [47,63,84,113,169]
        preset()
        
        
    r = []
    for i in range(0,6):
        n = random.randint(0,1535)
        r.append(n)
          
    if keypressed == ord('p'):
        preset_list = [r[0],r[1],r[2],r[3],r[4],r[5]]
        preset()
        
    elif keypressed == ord('l'):
        preset_list = [r[0],r[0],r[0],r[0],r[0],r[0]]
        preset()
    
    r = []
    for i in range(0,6):
        n = random.randint(50,450)
        r.append(n)
    
    if keypressed == ord('o'):
        hue_list = [r[0],r[1],r[2],r[3],r[4],r[5]]
        preset()
        
    elif keypressed == ord('k'):
        hue_list = [r[0],r[0],r[0],r[0],r[0],r[0]]
        preset()
        
    t = []
    for i in range(0,5):
        n = random.randint(0,255)
        t.append(n)
        t.sort()
    
    if keypressed == ord('i'):
        grayscale_list = t
        preset()
            
        '''
        EPILEPSY WARNING!!!
        '''
             
    if keypressed == ord('-'):
        
        preset_list = [c,b,a,z,y,x]
        preset()
        
    elif keypressed == ord('['):
        
        preset_list = [y,z,a,b,c,x]
        preset()
        
    elif keypressed == ord(']'):
        
        preset_list = [c,x,y,z,a,b]
        preset()
        
    elif keypressed == ord('`'):
        
        hue_list = [h1,h2,h3,h4,h5,h0]
        preset()
        
        '''
        These next keys are a memory recall function to save user presets.
        Q and W memorize all the trackbar positions.
        A and S recall Q and W.
        '''
        
    elif keypressed == ord('q'):
        
        save_list0 = [x,y,z,a,b,c]
        save_list1 = [h0,h1,h2,h3,h4,h5]
        save_list2 = [grayscale_break,grayscale_break2,grayscale_break3,grayscale_break4,grayscale_break5]
        
    elif keypressed == ord('w'):
        
        save_list3 = [x,y,z,a,b,c]
        save_list4 = [h0,h1,h2,h3,h4,h5]
        save_list5 = [grayscale_break,grayscale_break2,grayscale_break3,grayscale_break4,grayscale_break5]
        
    elif keypressed == ord('a'):
        
        preset_list = save_list0
        hue_list = save_list1
        grayscale_list = save_list2
        preset()
        
    elif keypressed == ord('s'):
        
        preset_list = save_list3
        hue_list = save_list4
        grayscale_list = save_list5
        preset()
        
        
    #uses the funky math function
    rgblist = funkyMath(x,h0)
    rgblist1 = funkyMath(y,h1)
    rgblist2 = funkyMath(z,h2)
    rgblist3 = funkyMath(a,h3)
    rgblist4 = funkyMath(b,h4)
    rgblist5 = funkyMath(c,h5)  
        
    #creates color papers
    red_paper[0:image_height,0:image_width, 0:image_channels] = rgblist
    yellow_paper[0:image_height,0:image_width, 0:image_channels] = rgblist1
    green_paper[0:image_height,0:image_width, 0:image_channels] = rgblist2
    cyan_paper[0:image_height,0:image_width, 0:image_channels] = rgblist3
    blue_paper[0:image_height,0:image_width, 0:image_channels] = rgblist4
    purple_paper[0:image_height,0:image_width, 0:image_channels] = rgblist5
    
    
    
    #display the current rgb values
    print(color("#1:",fore=(rgblist[2],rgblist[1],rgblist[0]),back=0),color(rgblist,fore=(rgblist[2],rgblist[1],rgblist[0]),back=0),
          color("  #2:",fore=(rgblist1[2],rgblist1[1],rgblist1[0]),back=0),color(rgblist1,fore=(rgblist1[2],rgblist1[1],rgblist1[0]),back=0),
          color("  #3:",fore=(rgblist2[2],rgblist2[1],rgblist2[0]),back=0),color(rgblist2,fore=(rgblist2[2],rgblist2[1],rgblist2[0]),back=0),
          color("  #4:",fore=(rgblist3[2],rgblist3[1],rgblist3[0]),back=0),color(rgblist3,fore=(rgblist3[2],rgblist3[1],rgblist3[0]),back=0),
          color("  #5:",fore=(rgblist4[2],rgblist4[1],rgblist4[0]),back=0),color(rgblist4,fore=(rgblist4[2],rgblist4[1],rgblist4[0]),back=0),
          color("  #6:",fore=(rgblist5[2],rgblist5[1],rgblist5[0]),back=0),color(rgblist5,fore=(rgblist5[2],rgblist5[1],rgblist5[0]),back=0))

    #grayscale limits
    min_grayscale_for_red = [0,0,0]
    max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_yellow = [grayscale_break+1,grayscale_break+1, 
                                grayscale_break+1]
    max_grayscale_for_yellow = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_green = [grayscale_break2+1, grayscale_break2+1,grayscale_break2+1]
    max_grayscale_for_green = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_cyan = [grayscale_break3+1,grayscale_break3+1,grayscale_break3+1]
    max_grayscale_for_cyan = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_blue = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    max_grayscale_for_blue = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_purple = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    max_grayscale_for_purple = [255,255,255]
    
    #format for grayscale values
    min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
    max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
    min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,
                                           dtype = "uint8")
    max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,
                                           dtype = "uint8")
    min_grayscale_for_green = numpy.array(min_grayscale_for_green, dtype = "uint8")
    max_grayscale_for_green = numpy.array(max_grayscale_for_green, dtype = "uint8")
    min_grayscale_for_cyan = numpy.array(min_grayscale_for_cyan, dtype = "uint8")
    max_grayscale_for_cyan = numpy.array(max_grayscale_for_cyan, dtype = "uint8")
    min_grayscale_for_blue = numpy.array(min_grayscale_for_blue, dtype = "uint8")
    max_grayscale_for_blue = numpy.array(max_grayscale_for_blue, dtype = "uint8")
    min_grayscale_for_purple = numpy.array(min_grayscale_for_purple, dtype = "uint8" )
    max_grayscale_for_purple = numpy.array(max_grayscale_for_purple, dtype = "uint8" )
    
    block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_red,
                                              max_grayscale_for_red)
    block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_yellow,
                                                 max_grayscale_for_yellow)
    block_all_but_the_green_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_green,
                                                 max_grayscale_for_green)
    block_all_but_the_cyan_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_cyan,
                                                 max_grayscale_for_cyan)
    block_all_but_the_blue_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_blue,
                                                 max_grayscale_for_blue)
    block_all_but_the_purple_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_purple,
                                                 max_grayscale_for_purple)
    
    red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
                                        mask = block_all_but_the_red_parts)
    yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
                                           mask = block_all_but_the_yellow_parts)
    green_parts_of_image = cv2.bitwise_or(green_paper, green_paper,
                                        mask = block_all_but_the_green_parts)
    cyan_parts_of_image = cv2.bitwise_or(cyan_paper, cyan_paper,
                                        mask = block_all_but_the_cyan_parts)
    blue_parts_of_image = cv2.bitwise_or(blue_paper, blue_paper,
                                        mask = block_all_but_the_blue_parts)
    purple_parts_of_image = cv2.bitwise_or(purple_paper,purple_paper, mask = block_all_but_the_purple_parts)
    
    #combine images
    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image2 = cv2.bitwise_or(green_parts_of_image, cyan_parts_of_image)
    customized_image3 = cv2.bitwise_or(blue_parts_of_image, purple_parts_of_image)
    customized_image4 = cv2.bitwise_or(customized_image, customized_image2)
    test_image = cv2.bitwise_or(customized_image3, customized_image4)
    
    #display images
    cv2.imshow('Customized Image',customized_image)
    cv2.imshow('Customized Image2', customized_image2)
    cv2.imshow('Customized Image3', customized_image3)
    cv2.imshow('Test Image', test_image)


keypressed = 2

#display original and final
cv2.destroyAllWindows()
cv2.namedWindow('Test Image')
cv2.namedWindow('Original Image')
cv2.imshow('Test Image', test_image)
cv2.imshow('Original Image', original_image)  


#image save loop
while keypressed !=27:

    keypressed = cv2.waitKey(1)    

    if keypressed == ord('s'):
    
        savefile.saveFile(test_image)
        
cv2.destroyAllWindows()

"""

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▄▄████████▀▄▄▄▄░░░░
░░░░░░░░░░▄█░█▄██░█▄██░░░░▀█░░░
░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀░░░░░▄░░░█░░░
░░░█▄▄░░░░░░░░░░░░░░░░░█░░░█░░░
░▄█████░░░░░░░░░░░░░░░░▀▄▄█▀░░░
░███████░░░░░░░░░░░░░░░░░░█░░░░
░██████▀░░░░░░░░░░░░░░░░░░█░░░░
░░████▀░░░░░░░░░░░░░░░░░░░█░░░░
░░░░█▄░░░░░░░░░░░░░░░░░░░░█░░░░
░░░░░░▀▀▀▀▀▀█▀▀▄▄░░░░░░░░▄█░░░░
░░░░░░░░░░░░██▄▄▄▄▄▄▄▄██████▄░░
░░░░░░░░░░░▄████████████▀▀░░█▄░
░░░░░░░░░░▄█░▀██▀░░░░░░░░░░░░█░
░░░░░░░░░░█░░░▀▀░░░░░░░▀█░░░░█░
░░░░░░░░░█░░░░░░░░░░░░░░█░░░░█░
░░░░░░░░░█░░░░░░░░░░░░░░█░░░░█░
░░░░░░░░█░░░░░░░░░░░░░░░█░░░░█░
░░░░░░░░█░░░░░░░░░░░░░░░█░░░░█░
░░░░░░░░█░░░░░░░░░░░░░░░█░░░░█░

"""
