from microbit import *

while True:
    if pin1.is_touched():
        display.show(Image.HEART)
    else:
        display.show(Image.SAD)
