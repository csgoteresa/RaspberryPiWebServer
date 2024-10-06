# boot.py -- run on boot-up
import network, utime

# Replace the following with your WIFI Credentials
SSID = "<WiFi SSID>"
SSI_PASSWORD = "<WiFi Password>"

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to the Network')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected. Network Config:', sta_if.ifconfig())
    
print("Connecting to your WiFi...")
do_connect()

