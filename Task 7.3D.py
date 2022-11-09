from tkinter import*
import tkinter.font                      # importing the font library for giving the different styles to the font
from gpiozero import LED
import RPi.GPIO
from tkinter
import time                              # import time library to get the current time in seconds, minutes, hours
import RPi.GPIO as GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)           # setting the pin mode system as BCM board in which we will direct refer to the GPIO pins

# defines the pins the ultrasonic sensor
GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(12, GPIO.OUT)              # setting the 12 pin as output pin which is PWM pin

led = GPIO.PWM(12, 500)               # setting the pin mode which gives variable frequency and then setting the duty cycle
led.start(0)                          # initial state of LED is LOW by giving the zero value to it

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)    # Setting the Trigger pin as output pin
GPIO.setup(GPIO_ECHO, GPIO.IN)        # Setting the echo pin as input pin

def Distance():
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.001)
    GPIO.output(GPIO_TRIGGER, False)
 
    TimeAtStart = time.time()
    TimeAtStop = time.time()
  
    while GPIO.input(GPIO_ECHO) == 0:
        TimeAtStart = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        TimeAtStop = time.time()
 
    TimeElapsed = TimeAtStop - TimeAtStart
    distance = (TimeElapsed * 34300) / 2             # calculates the distance
 
    return int(distance)                             # return the distance as the int type

try:                                         # it test our system code that we have written inside try
    while True:
        dis = Distance()                            # This is used to get the data from the Distance function
        print ("Measured Distance = " + str(dis) + " cm")           # prints the string which is written inside this command
        if dis < 50:                             # If distance is less than 50 then if condition willl execute
                led.ChangeDutyCycle((50 - dis)*2)
        else:
            led.start(0)                    # setting the brightness of LED as 0

        time.sleep(1)                       # giving a delay of 1 second
 
except KeyboardInterrupt:                   # throw an error if try doesn't execute
    GPIO.cleanup()                          # it will clean all the ports that we have used
