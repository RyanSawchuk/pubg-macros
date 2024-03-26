import pydirectinput as pdi
import keyboard as kb
import sys
import threading
import win32api
from time import sleep

pdi.PAUSE = 0
stop_key = '\\'
toggle_key = ']'
fire_key = '[' # second fire key in game
active = False

def run():
    global stop_key
    global toggle_key
    global fire_key
    global active
    while True:
        try:
            if win32api.GetKeyState(0x01) < 0 and active:
                pdi.press(fire_key)
                sleep(0.01)
            elif kb.is_pressed(toggle_key):
                active = not active
                print(f"ACTIVE: {active}")
                sleep(1)
            elif kb.is_pressed(stop_key):
                sys.exit(0)
            sleep(0.01)
        except Exception as e:
            pass

print('START - INACTIVE')

thread = threading.Thread(target=run)
thread.start()