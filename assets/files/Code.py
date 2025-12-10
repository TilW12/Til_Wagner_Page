
import Pin
import time


# pin definitions
pump = Pin(15, Pin.OUT)          # output to relay or MOSFET
button = Pin(14, Pin.IN, Pin.PULL_UP)  # button to GND

while True:
    if button.value() == 0:      # button pressed (active low)
        pump.value(1)            # turn pump on
    else:
        pump.value(0)            # turn pump off

    time.sleep(0.01)             # debounce delay
