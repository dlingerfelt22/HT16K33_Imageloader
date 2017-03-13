# Copyright (c) 2014 Adafruit Industries
# Author: David Lingerfelt
# Just give credit where credit is due.
# Adafruit made the LED backpack code. I made it better for my application. They removed the getKeys()
import time
import itertools
# itertools used for our infinite loop of rows
import pygame
# Loads our fullscreen images
from pygame.locals import *
from Adafruit_LED_Backpack import Matrix16x8
from copy import copy
from Adafruit_I2C import Adafruit_I2C
from Adafruit_LEDBackpack import LEDBackpack

# define subroutine to clean up the place
def cleanup():
    display.clear()
    display.write_display()
    start = time.time()
    oldKey = 0b00000000000000
    Key = 0b00000000000000
    extens = '.jpg'
    image1 = "img/" + "screensaver" + extens
    image1 = pygame.image.load(image1)
    # loads our image
    screen.fill((255,255,255))
    # In fullscreen
    screen.blit(image1,(0,0))
    pygame.display.flip()


#Initiate pygame even though we just use it to display images
pygame.init()
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
done = False

# Create a display with a specific I2C address and/or bus.
display = Matrix16x8.Matrix16x8(address=0x70, busnum=1)
keypad = LEDBackpack(address=0x71)

# Initialize the display and keypad
display.begin()

# Created lists of x,y iterated for each pest type.
PA = [1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6]
CA = [13, 3, 13, 4, 13, 5]
St = [1, 7, 1, 8, 2, 1, 2, 2, 2, 3]
Sd = [2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 3, 1, 3, 2, 3, 3, 3, 4]
Hc = [3, 5, 3, 6, 3, 7, 3, 8]
SB = [4, 1, 4, 2, 4, 3, 4, 4, 4, 5, 4, 6]
Md = [4, 7, 4, 8, 5, 1]
HF = [6, 1, 6, 2, 6, 3, 6, 4, 6, 5, 6, 6, 6, 7]
FF = [6, 8, 7, 1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6]
PSF = [7, 7, 7, 8, 8, 1, 8, 2, 8, 3, 8, 4, 8, 5]
FG = [5, 2, 5, 3, 5, 4, 5, 5, 5, 6]
GR = [8, 6, 8, 7, 8, 8, 9, 1, 9, 2]
AOR = [9, 3, 9, 4, 9, 5, 9, 6, 9, 7, 9, 8, 10, 1]
BB = [13, 6, 13, 7, 13, 8, 14, 1, 14, 2, 14, 3, 14, 4]
F = [14, 5, 14, 6, 14, 7]
SF = [5, 7, 5, 8]
M = [10, 2, 10, 3, 10, 4, 10, 5, 10, 6, 10, 7, 10, 8, 11, 1, 11, 2, 11, 3]
IMM = [11, 4, 11, 5, 11, 6, 11, 7, 11, 8]
PW = [14, 8, 15, 1, 15, 2, 15, 3, 15, 4, 15, 5, 15, 6]
YJ = [15, 7, 15, 8, 16, 1, 16, 2]
Mq = [16, 3, 16, 4, 16, 5, 16, 6, 16, 7]
R = [12, 1, 12, 2, 12, 3, 12, 4, 12, 5, 12, 6]
T = [12, 7, 12, 8, 13, 1, 13, 2]
BIC = [16, 8]

# I could not think of a better way to handle coordinating bug LEDs to key presses. So the index matches for the var version used in keyscanning.
ledBugList = [PA, CA, St, Sd, Hc, SB, Md, HF, FF, PSF, FG, GR, AOR, BB, F, SF, M, IMM, PW, YJ, Mq, R, T, BIC]
ledImgList = ['PA', 'CA', 'St', 'Sd', 'Hc', 'SB', 'Md', 'HF', 'FF', 'PSF', 'FG', 'GR', 'AOR', 'BB', 'F', 'SF', 'M', 'IMM', 'PW', 'YJ', 'Mq', 'R', 'T', 'BIC']

# Key scan values that have the row appended to it since that is not returned. 
PAVar = str(int(0b0000000000001))+str(0)
CAVar = str(int(0b0000000000010))+str(0)
StVar = str(int(0b0000000000100))+str(0)
SdVar = str(int(0b0000000001000))+str(0)
HcVar = str(int(0b0000000010000))+str(0)
SBVar = str(int(0b0000000100000))+str(0)
MdVar = str(int(0b0000001000000))+str(0)
HFVar = str(int(0b0000010000000))+str(0)
FFVar = str(int(0b0000100000000))+str(0)
PSFVar = str(int(0b0001000000000))+str(0)
FGVar = str(int(0b0000000000001))+str(1)
GRVar = str(int(0b0000000000010))+str(1)
AORVar = str(int(0b0000000000100))+str(1)
BBVar = str(int(0b0000000001000))+str(1)
FVar = str(int(0b0000000010000))+str(1)
SFVar = str(int(0b0000000100000))+str(1)
MVar = str(int(0b0000001000000))+str(1)
IMMVar = str(int(0b0000010000000))+str(1)
PWVar = str(int(0b0000100000000))+str(1)
YJVar = str(int(0b0001000000000))+str(1)
MqVar = str(int(0b0000000000001))+str(2)
RVar = str(int(0b0000000000010))+str(2)
TVar = str(int(0b0000000000100))+str(2)
BICVar = str(int(0b0000000001000))+str(2)

# List that has the number of rows in it.
rows = [0, 1, 2]

#indexed list for coordinating key press with bug type.
pestKeyList = [PAVar, CAVar, StVar, SdVar, HcVar, SBVar, MdVar, HFVar, FFVar, PSFVar, FGVar, GRVar, AORVar, BBVar, FVar, SFVar, MVar, IMMVar, PWVar, YJVar, MqVar, RVar, TVar, BICVar]
oldKey = 0b00000000000000
timer = 600

extens = '.jpg'
image1 = "img/" + "screensaver" + extens
image1 = pygame.image.load(image1)
# loads our image
screen.fill((255,255,255))
# In fullscreen
screen.blit(image1,(0,0))
pygame.display.flip()
start = time.time()

while not done:    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            display.clear()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
    #Main loop()
    for row in rows:
        time.sleep(0.1)
        key = keypad.getKeys(row)
        key = str(key) + str(row)
        if key != str(0) + str(row): 
            #test key against Var above
            for bug in pestKeyList:
                if key == bug:
                    if key != oldKey:
                        start = time.time()
                        print "key is " + key
                        stroke = pestKeyList.index(bug)
                        #set LEDset to bug LED array based on returned key.
                        LEDset = ledBugList[stroke]
                        LEDname = ledImgList[stroke]
                        # ADJUST TO PI FILE STRUCTURE
                        extens = '.jpg'
                        image1 = "img/" + LEDname + extens
                        image1 = pygame.image.load(image1)
                        # loads our image
                        screen.fill((255,255,255))
                        # In fullscreen
                        screen.blit(image1,(0,0))
                        pygame.display.flip()
                        display.clear()
                        a = 1
                        c = 2
                        for x in LEDset[::2]:
                            x = x - 1
                            print "x " + str(x)
                            y = LEDset[a:c]
                            print y
                            for b in y:
                                b = b - 1
                                print "y is " + str(b)
                                display.set_pixel(x, b, 1)
                            a = a + 2
                            c = c + 2
                        display.write_display()
                        oldKey = key
                    else:
                        end = time.time()
                        elapsed = end - start
                        pygame.display.flip()
                        if elapsed > timer:
                            cleanup()
        end = time.time()
        elapsed = end - start
        pygame.display.flip()
        if elapsed > timer:
            cleanup()
pygame.quit()
display.clear()

