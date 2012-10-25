#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from RGBDevice import RGBDevice

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(600)                        # Set frequency to 600 Hz

device = RGBDevice(pwm, 0)

def sleep():
  time.sleep(.01)

stepSize = 1

while (True):
  for red in range(0, 4095, stepSize):
    device.setRGB(red, 0, 0)
    sleep()
  device.setRGB(4095, 0, 0)
  time.sleep(1)
  for green in range(0, 4095, stepSize):
    device.setRGB(4095-green, green, 0)
    sleep()
  device.setRGB(0, 4095, 0)
  time.sleep(1)
  for blue in range(0, 4095, stepSize):
    device.setRGB(0, 4095-blue, blue)
    sleep()
  device.setRGB(0, 0, 4095)
  time.sleep(1)
  for red in range(0, 4095, stepSize):
    device.setRGB(red, 0, 4095-red)
    sleep()
  device.setRGB(4095, 0, 0)
  time.sleep(1)
  for white in range(0, 4095, stepSize):
    device.setRGB(4095, white, white)
    sleep()
  device.setRGB(4095, 4095, 4095)
  time.sleep(1)
  for white in range(0, 4095, stepSize):
    device.setRGB(4095-white, 4095-white, 4095-white)
    sleep()
  device.setRGB(0, 0, 0)
  time.sleep(1)

