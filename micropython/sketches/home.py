# Import required modules
import network
from machine import Pin
import BlynkLib

# Connect to Wi-Fi network
wifi_ssid = "Your_WiFi_SSID"
wifi_password = "Your_WiFi_Password"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_password)

while not sta_if.isconnected():
    pass

print("Wi-Fi connected:", sta_if.ifconfig())

# Connect to Blynk server
auth_token = "Your_Blynk_Auth_Token"

blynk = BlynkLib.Blynk(auth_token)

# Define pin numbers
led_pin = 2

# Initialize LED pin
led = Pin(led_pin, Pin.OUT)

# Define Blynk virtual pin handlers
@blynk.on("V0")
def v0_handler(value):
    if int(value[0]) == 1:
        led.value(1)
    else:
        led.value(0)

# Start Blynk loop
while True:
    blynk.run()
