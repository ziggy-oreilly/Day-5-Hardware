from microbit import *
import random

display.scroll("shake me")
while True:
    if accelerometer.was_gesture("shake"):
        sleep(1000)
        display.show(str(random.randint(1,6)))
    sleep(10)
