# Imports go at the top
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0, 8)


# Code in a 'while True:' loop repeats forever
while True:
    np = neopixel.NeoPixel(pin0, 8)
    np[0] = (63, 63, 0)
    np.show()