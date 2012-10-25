#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(600)                        # Set frequency to 60 Hz

master = 1

def setColor(red, green, blue):
  #print(str(red) + ', ' + str(green) + ', ' + str(blue))
  pwm.setPWM(1, 0, int(red * master))
  pwm.setPWM(2, 0, int(green * master))
  pwm.setPWM(0, 0, int(blue * master))

def sleep():
  time.sleep(.01)

stepSize = 1

while (True):
  for red in range(0, 4095, stepSize):
    setColor(red, 0, 0)
    sleep()
  setColor(4095, 0, 0)
  time.sleep(1)
  for green in range(0, 4095, stepSize):
    setColor(4095-green, green, 0)
    sleep()
  setColor(0, 4095, 0)
  time.sleep(1)
  for blue in range(0, 4095, stepSize):
    setColor(0, 4095-blue, blue)
    sleep()
  setColor(0, 0, 4095)
  time.sleep(1)
  for red in range(0, 4095, stepSize):
    setColor(red, 0, 4095-red)
    sleep()
  setColor(4095, 0, 0)
  time.sleep(1)
  for white in range(0, 4095, stepSize):
    setColor(4095, white, white)
    sleep()
  setColor(4095, 4095, 4095)
  time.sleep(1)
  for white in range(0, 4095, stepSize):
    setColor(4095-white, 4095-white, 4095-white)
    sleep()
  setColor(0, 0, 0)
  time.sleep(1)

