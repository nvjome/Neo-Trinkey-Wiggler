import time
import supervisor
import board
import neopixel
import touchio
import usb_hid
from adafruit_debouncer import Debouncer
from adafruit_hid.mouse import Mouse
from adafruit_ticks import ticks_ms, ticks_add, ticks_less

mouse = Mouse(usb_hid.devices)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)

touch1 = touchio.TouchIn(board.TOUCH1)
touch1DB = Debouncer(touch1)

wiggleState = False

wiggleInterval = 5000
wiggleNext = ticks_ms()

def wiggle():
    pixels[0] = (0, 5, 0)
    mouse.move(x=5)
    time.sleep(0.05)
    mouse.move(x=-5)
    time.sleep(0.05)
    pixels[0] = (0, 0, 0)

while True:
    touch1DB.update()

    if touch1DB.rose:
        wiggleState = not wiggleState

        if wiggleState:
            print("Wiggle on")
            pixels[0] = (0, 5, 0)
            time.sleep(0.2)
            pixels[0] = (0, 0, 0)
        else:
            print("Wiggle off")
            pixels[0] = (10, 0, 0)
            time.sleep(0.2)
            pixels[0] = (0, 0, 0)

    if wiggleState:
        if not ticks_less(ticks_ms(), wiggleNext):
            wiggleNext = ticks_add(ticks_ms(), wiggleInterval)
            wiggle()
            print("Wiggled")
