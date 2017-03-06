import time
import pygame 
from Adafruit_LED_Backpack import matrix8x16


# Alternatively, create a display with a specific I2C address and/or bus.
display = Matrix8x16.Matrix8x16(address=0x70, busnum=1)
keypad = Matrix8x16.Matrix8x16(address=0x71, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()
keypad.begin()

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
ledBugList = [PA, CA, St, Sd, Hc, SB, Md, HF, FF, PSF, FG, GR, AOR, BB, F, SF, M, IMM, PW, YJ, Mq, R, T, BIC]

PAVar = "0b00000000000010"
CAVar = "0b00000000000100"
StVar = "0b00000000001000"
SdVar = "0b00000000010000"
HcVar = "0b00000000100000"
SBVar = "0b00000001000000"
MdVar = "0b00000010000000"
HFVar = "0b00000100000000"
FFVar = "0b00001000000000"
PSFVar = "0b00010000000000"
FGVar = "0b00000000000011"
GRVar = "0b00000000000101"
AORVar = "0b00000000001001"
BBVar = "0b00000000010001"
FVar = "0b00000000100001"
SFVar = "0b00000001000001"
MVar = "0b00000010000001"
IMMVar = "0b00000100000001"
PWVar = "0b00001000000001"
YJVar = "0b00010000000001"
MqVar = "0b00000000000012"
RVar = "0b00000000000102"
TVar = "0b00000000001002"
BICVar = "0b00000000010002"

rows = [0, 1, 2]
pestKeyList = [PAVar, CAVar, StVar, SdVar, HcVar, SBVar, MdVar, HFVar, FFVar, PSFVar, FGVar, GRVar, AORVar, BBVar, FVar, SFVar, MVar, IMMVar, PWVar, YJVar, MqVar, RVar, TVar, BICVar]

#a[start_index:end_index:step]
while True:
    start = time.time()
    #Main loop()
    for row in rows:
        key = keypad.getKeys(row)
        #test key against Var above
        key = key + row
        for bug in pestKeyList:
            if key == bug:
                stroke = pestKeyList.index(bug)
                #set LEDset to bug LED array based on returned key.
                LEDset = ledBugList[stroke]
                print LEDset
                for x in LEDset[::2]:
                    for y in LEDset[1::2]:
                         # Clear the display buffer.
                         display.clear()
                         # Set pixel at position i, j to on.  To turn off a pixel set
                         # the last parameter to 0.
                         display.set_pixel(x, y, 1)
                         # Write the display buffer to the hardware.  This must be called to
                         # update the actual display LEDs.
                         display.write_display()
                else:
                    bugNum = bugNum + 1
        elapsed = (time.time() - start())
        if elapsed > 600:
        #do something about the time
        display.clear()
