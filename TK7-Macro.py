from pynput import keyboard
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import time
import os

forward = 'd'
back = 'a'

#class availables
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#def available
def clear_console():
    os.system('clear')

def BackDash():
    pressKey(key=back)
    time.sleep(0.02)
    pressKey(key="s")
    time.sleep(0.02)
    releaseKey(key="s")
    time.sleep(0.02)
    pressKey(key=forward)
    time.sleep(0.02)
    releaseKey(key=forward)
    time.sleep(0.02)
    releaseKey(key=back)

def WaveDash():
    pressKey(key=forward)
    time.sleep(0.02)
    releaseKey(key=forward)
    time.sleep(0.04)
    pressKey(key="s")
    time.sleep(0.02)
    pressKey(key=forward)
    time.sleep(0.02)
    releaseKey(key="s")
    time.sleep(0.02)
    releaseKey(key=forward)


def on_press(key):
    global forward
    global back
    try:
        if key == keyboard.Key.esc:
        # Stop listener
            print(bcolors.OKCYAN + "Aborting macro, quitting..." + bcolors.ENDC)
            return False
        elif key == keyboard.KeyCode(char = 'q'):
            BackDash()

        elif key == keyboard.KeyCode(char = 'e'):
            WaveDash()

        elif key == keyboard.KeyCode(char = 'f'):
            
            if forward == 'd':
                forward = 'a'
                back = 'd'
            elif forward == 'a':
                forward = 'd'
                back = 'a'

    except AttributeError:
        pass

def on_release(key):
    pass

clear_console()
print("")
print("")
print("████████ ███████ ██   ██ ██   ██ ███████ ███    ██     ███████     ███    ███  █████   ██████ ██████   ██████  ")
print("   ██    ██      ██  ██  ██  ██  ██      ████   ██          ██     ████  ████ ██   ██ ██      ██   ██ ██    ██ ")
print("   ██    █████   █████   █████   █████   ██ ██  ██         ██      ██ ████ ██ ███████ ██      ██████  ██    ██ ")
print("   ██    ██      ██  ██  ██  ██  ██      ██  ██ ██        ██       ██  ██  ██ ██   ██ ██      ██   ██ ██    ██ ")
print("   ██    ███████ ██   ██ ██   ██ ███████ ██   ████        ██       ██      ██ ██   ██  ██████ ██   ██  ██████  ")
print("                                                                                                               ")
print("")
print("[Q] for Backdash")
print("[E] for Wavedash")
print("[F] for P1/P2 side")
print("[ESC] for quitting")
print("")
print(bcolors.WARNING + "Macro is running..." + bcolors.ENDC)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

