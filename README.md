# Neo-Trinkey-Wiggler

Yet another mouse wiggler/jiggler/shaker/mover, because there aren't enough of these floating around...

The Adafruit Neo Trinkey lends itself well to this purpose due to its small size and built-in USB A plug. I also thought the capacitive touchpads were pretty cool.

The `boot.py` disables the serial port and storage drive to keep things clean for normal use. If touchpad 2 is pressed while the blue LED is still on, the serial port and storage drive are enabled for development purposes.

Pressing touchpad 1 enalbed the wiggling, pressing again disables it.

The libraries in the `lib`  folder are pulled from the [official Adafruit CircuitPython library bundle](https://circuitpython.org/libraries) and I do not claim ownership or any copyrights over them. These are for version 8.x, differnt CircuitPython versions will need the corresponding library versions.
