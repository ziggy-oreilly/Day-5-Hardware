from microbit import *

compass.calibrate()
display.scroll("Lets go!")

while True:
    x = compass.heading()
    if x > 315 or x <= 45:
        display.show("N")
    if x > 45 and x <= 135:
        display.show("E")
    if x > 135 and x <= 225:
        display.show("S")
    if x >225 and x <=315:
        display.show("W")