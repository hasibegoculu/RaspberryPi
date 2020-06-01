#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
## Author: Hasibe 
## Re-used this code for my small projects. - 29.05.2020

import RPi.GPIO as GPIO
import time

ledPin = 11    # define ledPin

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    print ('using pin%d'%ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
        print ('led turned on >>>')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(ledPin, GPIO.LOW)   # make ledPin output LOW level to turn off led
        print ('led turned off <<<')
        time.sleep(1)                   # Wait for 1 second

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()




###
### There is another version of the same code.. Shorter...
'''
from gpiozero import LED
from time import sleep

print ('Program is starting ... ')

led = LED(17)           # define LED pin according to BCM Numbering

while True:
    led.on()    # turn on LED
    print ('led turned on >>>')  # print message on terminal
    sleep(1)    # wait 1 second
    led.off()   # turn off LED 
    print ('led turned off <<<')
    sleep(1)    # wait 1 second
'''