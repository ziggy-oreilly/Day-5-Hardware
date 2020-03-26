# Cabe Atwell - Microbit metal detector
# https://www.element14.com/community/community/stem-academy/microbit/blog/2018/09/06/project-bbc-microbit-metal-detector

from microbit import *

sensitivity = 2500 # 2500 is a good start.
# You can adjust this number depending on how much metal
# you want to sense in any one spot.

# images to show for various field levels
# The images correspond with how much is detected.

imgs =\
(Image("00000:"
      "00400:"
      "04940:"
      "00400:"
      "00000"),
Image("00000:"
      "04940:"
      "09990:"
      "04940:"
      "00000"),
Image("03530:"
      "39993:"
      "59995:"
      "39993:"
      "03530"),
Image("49994:"
      "99999:"
      "99999:"
      "99999:"
      "49994"))

# initial values, like zero level
x_start = compass.get_x()
y_start = compass.get_y()
z_start = compass.get_z()

while True:

    if button_a.is_pressed() or button_b.is_pressed(): # update the zero level
        sleep(1000)
        x_start = compass.get_x() # This means whatever value is sensed here, is now a
        y_start = compass.get_y() # theoretical zero.
        z_start = compass.get_z()

    x = compass.get_x() - x_start # Check sensor
    if x<0: x=-x # absolute value

    y = compass.get_y() - y_start
    if y<0: y=-y # absolute value

    z = compass.get_z() - z_start
    if z<0: z=-z # absolute value

    # find a maximum value. This will check is an one value spiked
    fs=z
    if fs<y: fs=y
    if fs<x: fs=x

    # pixel in the center
    img = Image("00000:"
             "00000:"
             "00900:"
             "00000:"
             "00000")

    # if field strength high enough, then show corresponding image
    if fs>(sensitivity*7): img = imgs[3]
    elif fs>(sensitivity*3): img = imgs[2]
    elif fs>(sensitivity*1.5): img = imgs[1]
    elif fs>sensitivity: img = imgs[0]

    display.show(img)

    sleep(10) # time in milleseconds, it define images update rate