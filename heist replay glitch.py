"""===GTA V HEIST REPLAY GLITCH===
        *Author = Blur#6421*
"""

import os
import keyboard

toggle = False

print("Heist Replay Glitch | PRESS N")

while True:
    if keyboard.is_pressed("n"):
        if toggle == False:
            print('N presed. Stopping connection')
            os.system("netsh interface set interface Ethernet disabled") # Change "Ethernet" for your network interface's name
            toggle = True
        else:
            print('Restoring connection')
            os.system("netsh interface set interface Ethernet enabled") # Change "Ethernet" for your network interface's name