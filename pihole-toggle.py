#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import sys
import time

print "PiHole Configuration for External Switch"

# switch connected between ground and pin 27
switchPin = 27 # the pin for the switch input

GPIO.setmode(GPIO.BCM) # sets pin numbering scheme to BCM mode
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def setEnabled(state):
  print "setEnabled", state
  GPIO.remove_event_detect(switchPin)

  if state == True:
    print "pihole enable"
    subprocess.call(['pihole', 'enable'], shell=False)
    GPIO.add_event_detect(switchPin, GPIO.RISING, callback=disable, bouncetime=300)
  else:
    print "pihole disable"
    subprocess.call(['pihole', 'disable'], shell=False)
    GPIO.add_event_detect(switchPin, GPIO.FALLING, callback=enable, bouncetime=300)

def enable(channel):
	setEnabled(True)
def disable(channel):
	setEnabled(False)

# make the state consistent with the toggle button
isEnabled = not GPIO.input(switchPin) # true if pin is grounded
setEnabled(isEnabled)

# sleep instead of exiting the program
try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  print("\nUser pressed Ctrl-C")
finally:
  GPIO.cleanup()         # clean up GPIO on CTRL+C exit
  sys.exit(0)

print "clean exit"
GPIO.cleanup()           # clean up GPIO on normal exit