import storage
import usb_cdc
import time
import supervisor
import board
import neopixel
import touchio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

timePrev = 0
interval = 1500

timePrev = supervisor.ticks_ms()

# disable console and drive by default for normal use
usb_cdc.disable()
storage.disable_usb_drive()

pixels.fill((0,0,10))

while True:
    # if touched within the interval, enable console and storage for development
    timeNow = supervisor.ticks_ms()

    if timeNow - timePrev >= interval:
        # timed out
        pixels.fill((10,0,0))
        time.sleep(0.2)
        break
    
    if touch2.value:
        usb_cdc.enable()
        storage.enable_usb_drive()
        pixels.fill((0,10,0))
        time.sleep(0.8)
        break

pixels.fill((0,0,0))