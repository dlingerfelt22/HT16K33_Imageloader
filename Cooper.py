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

# define subroutine to clean up the place
def cleanup():
    display.clear()
    start = time.time()
    oldKey = "0b00000000000000"
    newKey = "0b00000000000000"

class LEDBackpack:
  i2c = None

  # Registers
  __HT16K33_REGISTER_DISPLAY_SETUP        = 0x80
  __HT16K33_REGISTER_SYSTEM_SETUP         = 0x20
  __HT16K33_REGISTER_DIMMING              = 0xE0

  # Data base addresses
  __HT16K33_ADDRESS_KEY_DATA              = 0x40

  # Blink rate
  __HT16K33_BLINKRATE_OFF                 = 0x00
  __HT16K33_BLINKRATE_2HZ                 = 0x01
  __HT16K33_BLINKRATE_1HZ                 = 0x02
  __HT16K33_BLINKRATE_HALFHZ              = 0x03

  # Constructor
  def __init__(self, address=0x71, debug=False):
    self.i2c = Adafruit_I2C(address)
    self.address = address
    self.debug = debug

  def getKeys(self, row):
    "Returns a row of scanned key press values as a single 13-bit value (K13:K1)"
    if (row > 2):
      return
    return self.i2c.readU16(self.__HT16K33_ADDRESS_KEY_DATA + row*2)

#Initiate pygame even though we just use it to display images
pygame.init()
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)


# Create a display with a specific I2C address and/or bus.
display = Matrix16x8.Matrix16x8(address=0x70, busnum=1)
keypad = LEDBackpack(address=0x71, debug=False)

# Initialize the display and keypad
display.begin()
keypad.begin()

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
PAVar = str(int(0b0000000000001))+str(1)
CAVar = str(int(0b0000000000010))+str(1)
StVar = str(int(0b0000000000100))+str(1)
SdVar = str(int(0b0000000001000))+str(1)
HcVar = str(int(0b0000000010000))+str(1)
SBVar = str(int(0b0000000100000))+str(1)
MdVar = str(int(0b0000001000000))+str(1)
HFVar = str(int(0b0000010000000))+str(1)
FFVar = str(int(0b0000100000000))+str(1)
PSFVar = str(int(0b0001000000000))+str(1)
FGVar = str(int(0b0000000000001))+str(2)
GRVar = str(int(0b0000000000010))+str(2)
AORVar = str(int(0b0000000000100))+str(2)
BBVar = str(int(0b0000000001000))+str(2)
FVar = str(int(0b0000000010000))+str(2)
SFVar = str(int(0b0000000100000))+str(2)
MVar = str(int(0b0000001000000))+str(2)
IMMVar = str(int(0b0000010000000))+str(2)
PWVar = str(int(0b0000100000000))+str(2)
YJVar = str(int(0b0001000000000))+str(2)
MqVar = str(int(0b0000000000001))+str(3)
RVar = str(int(0b0000000000010))+str(3)
TVar = str(int(0b0000000000100))+str(3)
BICVar = str(int(0b0000000001000))+str(3)

# List that has the number of rows in it.
rows = [0, 1, 2]

#indexed list for coordinating key press with bug type.
pestKeyList = [PAVar, CAVar, StVar, SdVar, HcVar, SBVar, MdVar, HFVar, FFVar, PSFVar, FGVar, GRVar, AORVar, BBVar, FVar, SFVar, MVar, IMMVar, PWVar, YJVar, MqVar, RVar, TVar, BICVar]
oldKey = "0b00000000000000"
#a[start_index:end_index:step]
while True:
    start = time.time()
    #Main loop()
    for row in itertools.cycle(rows):
        key = keypad.getKeys(row)
        if key != 0: 
            #test key against Var above
            key = str(key) + str(row)
            for bug in pestKeyList:
                if key == bug:
                    newKey = key
                    if newKey != oldKey:
                        start = time.time()
                        stroke = pestKeyList.index(bug)
                        #set LEDset to bug LED array based on returned key.
                        LEDset = ledBugList[stroke]
                        LEDname = ledImgList[stroke]
                        # ADJUST TO PI FILE STRUCTURE
                        extens = '.jpg'
                        image1 = "img\\" + LEDname + extens
                        image1 = pygame.image.load(image1)
                        # loads our image
                        screen.fill((255,255,255))
                        # In fullscreen
                        screen.blit(image1,(0,0))
                        pygame.display.flip()
                        for x in LEDset[::2]:
                            x = x - 1
                            for y in LEDset[1::2]:
                                 y = y - 1
                                 # Clear the display buffer.
                                 display.clear()
                                 # Set pixel at position i, j to on.  To turn off a pixel set
                                 # the last parameter to 0.
                                 display.set_pixel(x, y, 1)
                                 # Write the display buffer to the hardware.  This must be called to
                                 # update the actual display LEDs.
                                 display.write_display()
                        oldKey = key
                    else:
                        elapsed = (time.time() - start())
                        if elapsed > 600:
                            cleanup()
        else:
            elapsed = (time.time() - start())
            if elapsed > 600:
                cleanup()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
pygame.quit()
