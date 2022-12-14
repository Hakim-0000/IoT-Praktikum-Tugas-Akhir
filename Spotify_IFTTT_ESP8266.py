#############################
######### Hakim0000 #########
#############################

from machine import Pin
import time
import network
import urandom as random
import urequests as requests

## Var Wi-Fi
SSID = 'SSID' ## input your SSID name
Password = 'sup3rs3cur3' ## input your SSID password
reset = True

## Machine
p0 = Pin(2, Pin.OUT)
blinker = 0

## WebHook URL API
play_api = 'https://maker.ifttt.com/trigger/play_spotify/json/with/key/k8LDDGBQ69J3y_N74aTu2gbXk3TZl0LVm82cFTRRcrZ'
pause_api = 'https://maker.ifttt.com/trigger/pause_spotify/json/with/key/k8LDDGBQ69J3y_N74aTu2gbXk3TZl0LVm82cFTRRcrZ'
skip_api = 'https://maker.ifttt.com/trigger/skip_spotify/json/with/key/k8LDDGBQ69J3y_N74aTu2gbXk3TZl0LVm82cFTRRcrZ'

## Short Blink 50ms
def blinkShort():
    p0.value(0)
    time.sleep_ms(100)
    p0.value(1)
    time.sleep_ms(100)
    
## Normal Blink 1s
def blinkNormal():
    p0.value(0)
    time.sleep(1)
    p0.value(1)
    time.sleep(1)
    
## Play function
def play():
    play_spt = requests.post(play_api)
    if(play_spt.status_code==200):
        print('$  Spotify is now playing!')
        blinkShort()
    else:
        print('$  Failed to play Spotify')
        blinkNormal()
    play_spt.close()

## Pause function
def pause():
    pause_spt = requests.post(pause_api)
    if(pause_spt.status_code==200):
        print('$  Spotify is paused!')
        blinkShort()
    else:
        print('$  Failed to pause Spotify')
        blinkNormal()
    pause_spt.close()
    
## Skip function
def skip():
    skip_spt = requests.post(skip_api)
    if(skip_spt.status_code==200):
        print('$  Skipped to the next song!')
        blinkShort()
    else:
        print('$ Failed to skip song')
        blinkNormal()
    skip_spt.close()

## Wi-Fi Connect
def connectWLAN():
    wlan0 = network.WLAN(network.STA_IF)
    if reset:
        wlan0.active(True)
        
        ## Connect to given ssid
        wlan0.connect(SSID, Password)
        
        ## Failed to connect
        while not wlan0.isconnected():
            wlan0.active(True)
            pass
        
    status = wlan0.isconnected()
    ip_addr = wlan0.ifconfig()
    return status, ip_addr

## Main
def main():
    print('$ Starting ESP8266 . . . .')
    print(f'$ Connecting to {SSID}')
    status, ip_addr = connectWLAN()
    
    if(status == True):
        print(f'$ Connected to {SSID}')
        act = input('$ What you wanna do?\n  -Play\n  -Pause\n  -Skip\n  >')
        if(act.lower()=='play'):
            play()
            print('')
            
        elif(act.lower()=='pause'):
            pause()
            print('')
        
        elif(act.lower()=='skip'):
            skip()
            print('')
    else:
        print(f'==> Failed to connect to {SSID}')
        
main()