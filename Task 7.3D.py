from tkinter import*
import tkinter.font                      # importing the font library for giving the different styles to the font
from gpiozero import LED                 # imported to use the button interface in the code
import RPi.GPIO                          
from tkinter
import time                              # import time library to get the current time in seconds, minutes, hours
import RPi.GPIO as GPIO                  # we are just refering to the GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)           # setting the pin mode system as BCM board in which we will direct refer to the GPIO pins

GPIO_TRIGGER = 18                        # defines the pins the ultrasonic sensor
GPIO_ECHO = 24

GPIO.setup(12, GPIO.OUT)                 # setting the 12 pin as output pin which is PWM pin

led = GPIO.PWM(12, 100)                  # setting the pin mode which gives variable frequency and then setting the duty cycle
led.start(0)                             # initial state of LED is LOW by giving the zero value to it

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)       # Setting the Trigger pin as output pin
GPIO.setup(GPIO_ECHO, GPIO.IN)           # Setting the echo pin as input pin

def Distance():
    GPIO.output(GPIO_TRIGGER, True)                  # giving the value of trigger pin as true 
 
    time.sleep(0.001)                                # giving a delay
    GPIO.output(GPIO_TRIGGER, False)                 # giving the value of trigger pin as False 

    TimeAtStart = time.time()
    TimeAtStop = time.time()
  
    while GPIO.input(GPIO_ECHO) == 0:                # iterates in this loop while the its value is zero
        TimeAtStart = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:                # iterates in this loop while the its value is one
        TimeAtStop = time.time()
 
    TimeElapsed = TimeAtStop - TimeAtStart           # getting the value of TimeElapsed by subtracting the these two values
    distance = (TimeElapsed * 34300) / 2             # calculates the distance
 
    return int(distance)                             # return the distance as the int type

try:                                                                # it test our system code that we have written inside try
    while True:                                                     # this loop iterates untill any error comes
        dis = Distance()                                            # This is used to get the data from the Distance function
        print ("Measured Distance = " + str(dis) + " cm")           # prints the string which is written inside this command
        if dis < 50:                                                # If distance is less than 50 then if condition willl execute
                led.ChangeDutyCycle((50 - dis)*2)                   # changing the value of duty cycle of LED as the distance value varies
        else:
            led.start(0)                                            # setting the brightness of LED as 0

        time.sleep(1)                                               # giving a delay of 1 second
 
except KeyboardInterrupt:                                   # throw an error if try doesn't execute
    GPIO.cleanup()                                          # it will clean all the ports that we have used
