from microbit import *

while True:
    temp = temperature()
    if temp >= 30:
        display.scroll(temp)
        display.scroll("HOT!")
    if temp >= 20 and temp < 30:
        display.scroll(temp)
        display.scroll("GOOD!")
    if temp < 20:
        display.scroll(temp)
        display.scroll("COLD")