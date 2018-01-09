import time
"""
Pin Labels

D0 = 16;
D1 = 5;
D2 = 4;
D3 = 0;
D4 = 2;
D5 = 14;
D6 = 12;
D7 = 13;
D8 = 15;
D9 = 3;
D10 = 1;

"""

"""
PD5 = Pin(14,Pin.OUT)
PD6 = Pin(12,Pin.OUT)
PD7 = Pin(13,Pin.OUT)
DP9 = Pin(3,Pin.OUT)
DP10 = Pin(1,Pin.OUT)
"""

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    
    if not wlan.isconnected():
        ID = str(input("Enter SSID: "))
        Pass = str(input("Enter Pass: "))
        
        wlan.active(True)
        wlan.connect(ID,Pass)
        deadline = time.ticks_add(time.ticks_ms(),30000)
        while not(wlan.isconnected() or not (time.ticks_diff(deadline,time.ticks_ms())> 0)):
            print('Connection to WIFI')

        print('network config:', wlan.ifconfig())
    else:
        print('network config:',wlan.ifconfig())

    if wlan.isconnected():
        return 1
    else:
        return 0


