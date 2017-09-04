#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess

# Use the board numbering scheme
GPIO.setmode(GPIO.BOARD)
# Turn off warnings
GPIO.setwarnings(False)

# Define pins
power_pin = 5
fan_pin = 13
led_pin = 40

# Set up pin sand enable the pull up resistor
GPIO.setup(power_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(fan_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

# Turn on the fan and LED at boot
GPIO.output(fan_pin, GPIO.HIGH)
GPIO.output(led_pin, GPIO.HIGH)

# Initialize the previous state
old_state = True
while True:
    # Get the state of the pin
    switch_state = GPIO.input(power_pin)
    # If the state has changed and the state is now True
    if switch_state != old_state and switch_state == True:
        # Turn off the fan
        GPIO.output(fan_pin, GPIO.LOW)
        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        GPIO.cleanup()
        # Call a system halt
        subprocess.call("halt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    old_state = switch_state
    # Rest the process
    time.sleep(0.1)
