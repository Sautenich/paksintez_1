"""
paksintez_1 base module.

This is the principal module of the paksintez_1 project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

# example constant variable
NAME = "paksintez_1"

import RPi.GPIO as GPIO
import time
input_pin=18

def main(): 
    prev_value = None 
 
    # Pin Setup: 
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi 
    GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin 
    print("Starting demo now! Press CTRL+C to exit") 
    try: 
        while True: 
            value = GPIO.input(input_pin) 
            if value != prev_value: 
                if value == GPIO.HIGH: 
                    value_str = "HIGH" 
                else: 
                    value_str = "LOW" 
                print("Value read from pin {} : {}".format(input_pin, 
                                                           value_str)) 
                prev_value = value 
            time.sleep(1) 
    finally: 
        GPIO.cleanup() 
 
if name == '__main__': 
    main()