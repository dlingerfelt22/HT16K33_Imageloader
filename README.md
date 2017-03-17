# HT16K33_Imageloader
Loads images from getkey() and drives a second HT16K33 with 128 LEDs

This is using the Adafruit 16x8 LED driver HT16K33 breakout found here:
https://www.adafruit.com/product/1427

The scope of this project is to control a group of 128 LEDs, all corresponding to a pest type and location in a simulated structure (i.e. a toy house). There is a keypad that is running on a matrix using the same type of HT16K33 and 30 momentary switches. When a button is pressed an image is loaded and the corresponding LEDs light up.

We will be using pygame to load the images.
Adafruits library for LED backpacks found here:
https://github.com/adafruit/Adafruit_Python_LED_Backpack.git

We will also be using a library written by  https://github.com/nonflammable at
https://github.com/nonflammable/Adafruit_Python_LED_Backpack/blob/db2d8f76145436490925712205058fe74b115843/Adafruit_LED_Backpack/Matrix16x8.py

I am a hobbyist programmer, if you read my code and want to help. I would love it!

The adafruit libraries used are broken for getkeys() and python 2 libraries are used while loading the 16x8 from the Adafruit_LED_Backpack the rest of the code is from Adafruit_LEDBackpack... So watch your _
