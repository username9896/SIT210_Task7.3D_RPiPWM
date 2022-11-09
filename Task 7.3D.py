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

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)    # Setting the Trigger pin as 
GPIO.setup(GPIO_ECHO, GPIO.IN)

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
    distance = (TimeElapsed * 34300) / 2
 
    return int(distance)

try:
    while True:
        dis = Distance()
        print ("Measured Distance = " + str(dis) + " cm")
        if dis < 50:
                led.ChangeDutyCycle((50 - dis)*2)
        else:
            led.start(0)

        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()
