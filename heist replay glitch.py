"""===GTA V HEIST REPLAY GLITCH===
        *Author = Blur#6421*
"""

import os
import keyboard

toggle = False

with open("settings.cfg", 'r') as f:
    settings = f.readlines()

nsetting = [setting.strip() for setting in settings]

print("Heist Replay Glitch | PRESS N")

while True:
    if keyboard.is_pressed("n"):
        if toggle == False:
            print('N presed. Stopping connection')
            os.system(f"netsh interface set interface {nsetting[0]} disabled")
            toggle = True
        else:
            print('Restoring connection')
            os.system(f"netsh interface set interface {nsetting[0]} enabled")
            toggle = False