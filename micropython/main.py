import machine
import time

led_pin = machine.Pin(2, machine.Pin.OUT)
while True:
    led_pin.value(1)
    print("LED ON...")
    time.sleep(1)
    led_pin.value(0)
    print("LED OFF...")
    time.sleep(1)