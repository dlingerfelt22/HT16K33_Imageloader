# HT16K33_Imageloader
Loads images from getkey() and drives a second HT16K33 with 128 LEDs

This is using the Adafruit 16x8 LED driver HT16K33 breakout found here:
https://www.adafruit.com/product/1427

The scope of this progect is to control a group of 128 LEDs, all corresponding to a pest type and location in a simulated structure (i.e. a toy house). There is a keypad that is running on a matrix using the same HT16K33 and 30 momentary switches. When a button is pressed an image is loaded and the corresponding LEDs light up.

We will be using pygame to load the images.
Adafruits library for LED backpacks found here:
https://github.com/adafruit/Adafruit_Python_LED_Backpack.git

I am far from a professional programmer, if you read my code and want to help. I would love it!
