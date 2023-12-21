import network

print("Started")

WIFI_NETWORK='SUPERONLINE_WiFi_2AA5'

WIFI_PASSWORD='TKWEFME9NPYJ'


wlan = network.WLAN(network.STA_IF)

wlan.active(True)

wlan.connect(WIFI_NETWORK, WIFI_PASSWORD)


print()

print("Connected to ",WIFI_NETWORK)
