import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
RELAY = 17

tank_height = 30

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(RELAY, GPIO.OUT)

while True:

    GPIO.output(TRIG, False)
    time.sleep(0.2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        start=time.time()

    while GPIO.input(ECHO)==1:
        stop=time.time()

    distance=(stop-start)*17150

    level=(tank_height-distance)/tank_height*100

    level=max(0,min(100,level))

    print("Water Level:",level,"%")

    if level <= 20:
        GPIO.output(RELAY,0)

    if level >= 100:
        GPIO.output(RELAY,1)

    time.sleep(3)