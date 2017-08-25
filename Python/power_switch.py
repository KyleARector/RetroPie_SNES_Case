#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess

# Use the board numbering scheme
GPIO.setmode(GPIO.BOARD)
# Set up pin 5 as an input and enable the pull up resistor
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the previous state
old_state = True
while True:
    # Get the state of the pin
    switch_state = GPIO.input(5)
    # If the state has changed and the state is now True
    if switch_state != old_state and switch_state == True:
        # Call a system halt
        subprocess.call("halt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    old_state = switch_state
    # Rest the process
    time.sleep(0.1)
