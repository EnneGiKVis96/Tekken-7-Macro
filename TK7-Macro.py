from pynput import keyboard
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import time
import os
import threading

forward = 'd'
back = 'a'
profile = "generic"

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

def OTGF1():
    pressKey(key="NUM4")
    time.sleep(0.02)
    releaseKey(key="NUM4")
    press(key="NUMLOCK")

def PEWGF1():
    pressKey(key=forward)
    time.sleep(0.02)
    releaseKey(key=forward)
    time.sleep(0.02)

def EWGF1():
    pressKey(key=forward)
    time.sleep(0.02)
    releaseKey(key=forward)
    time.sleep(0.05)
    pressKey(key="s")
    time.sleep(0.1)
    releaseKey(key="s")

def EWGF2():
    pressKey(key="s")
    time.sleep(0.02)
    releaseKey(key="s")

def EWGF3():
    pressKey(key=forward)
    time.sleep(0.02)
    releaseKey(key=forward)

def EWGF4():
    pressKey(key="NUM8")
    time.sleep(0.02)
    releaseKey(key="NUM8")
    press(key="NUMLOCK")

def iWR2():
    pressKey(key=forward)
    time.sleep(0.002)
    releaseKey(key=forward)
    time.sleep(0.002)
    pressKey(key=forward)
    time.sleep(0.002)
    releaseKey(key=forward)
    time.sleep(0.002)
    pressKey(key=forward)
    time.sleep(0.002)
    pressKey(key="NUM8")
    time.sleep(0.002)
    releaseKey(key=forward)
    releaseKey(key="NUM8")
    time.sleep(0.002)
    press(key="NUMLOCK")

def iShiningWizard1():
    pressKey(key=forward)
    time.sleep(0.002)
    releaseKey(key=forward)
    time.sleep(0.002)
    pressKey(key=forward)
    time.sleep(0.002)
    releaseKey(key=forward)
    time.sleep(0.002)
    pressKey(key=forward)
    time.sleep(0.002)
    x = threading.Thread(target=iShiningWizard2)
    y = threading.Thread(target=iShiningWizard3)
    x.start()
    y.start()
    time.sleep(0.002)
    releaseKey(key=forward)
    time.sleep(0.002)
    press(key="NUMLOCK")

def iShiningWizard2():
    pressKey(key="NUM8")
    time.sleep(0.002)
    releaseKey(key="NUM8")

def iShiningWizard3():
    pressKey(key="NUM6")
    time.sleep(0.002)
    releaseKey(key="NUM6")

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

        elif profile == 'kazuya':
            if key == keyboard.KeyCode(char = '7'):
                x = threading.Thread(target=PEWGF1)
                y = threading.Thread(target=EWGF2)
                z = threading.Thread(target=EWGF3)
                u = threading.Thread(target=EWGF4)
                x.start()
                time.sleep(0.05)
                y.start()
                z.start()
                u.start()

            elif key == keyboard.KeyCode(char = '9'):
                x = threading.Thread(target=EWGF1)
                y = threading.Thread(target=EWGF2)
                z = threading.Thread(target=EWGF3)
                u = threading.Thread(target=EWGF4)
                x.start()
                time.sleep(0.12)
                y.start()
                z.start()
                u.start()

        elif profile == 'heihachi':
            if key == keyboard.KeyCode(char = '7'):
                x = threading.Thread(target=PEWGF1)
                y = threading.Thread(target=EWGF2)
                z = threading.Thread(target=EWGF3)
                u = threading.Thread(target=OTGF1)
                x.start()
                time.sleep(0.05)
                y.start()
                z.start()
                u.start()
            
            elif key == keyboard.KeyCode(char = '9'):
                x = threading.Thread(target=EWGF1)
                y = threading.Thread(target=EWGF2)
                z = threading.Thread(target=EWGF3)
                u = threading.Thread(target=EWGF4)
                x.start()
                time.sleep(0.12)
                y.start()
                z.start()
                u.start()

        elif profile == 'jin':
            if key == keyboard.KeyCode(char = '9'):
                x = threading.Thread(target=EWGF1)
                y = threading.Thread(target=EWGF2)
                z = threading.Thread(target=EWGF3)
                u = threading.Thread(target=EWGF4)
                x.start()
                time.sleep(0.12)
                y.start()
                z.start()
                u.start()

        elif profile == 'dragunov':
            if key == keyboard.KeyCode(char = '9'):
                iWR2()

        elif profile == 'king':
            if key == keyboard.KeyCode(char = '9'):
                iShiningWizard1()

    except AttributeError:
        pass

def on_release(key):
    pass

def appTitle():
    print(bcolors.OKGREEN + "")
    print("")
    print("████████ ███████ ██   ██ ██   ██ ███████ ███    ██     ███████     ███    ███  █████   ██████ ██████   ██████  ")
    print("   ██    ██      ██  ██  ██  ██  ██      ████   ██          ██     ████  ████ ██   ██ ██      ██   ██ ██    ██ ")
    print("   ██    █████   █████   █████   █████   ██ ██  ██         ██      ██ ████ ██ ███████ ██      ██████  ██    ██ ")
    print("   ██    ██      ██  ██  ██  ██  ██      ██  ██ ██        ██       ██  ██  ██ ██   ██ ██      ██   ██ ██    ██ ")
    print("   ██    ███████ ██   ██ ██   ██ ███████ ██   ████        ██       ██      ██ ██   ██  ██████ ██   ██  ██████  ")
    print("                                                                                                               ")
    print("")


def menuStart():

    global profile
    clear_console()
    appTitle()

    print("[1] Kazuya")
    print("[2] Heihachi")
    print("[3] Jin/DevilJin")
    print("[4] Claudio/Dragunov")
    print("[5] King/Armor King")
    print("[6] Generic")
    print("[7] Exit")
    print("")
    choice = input(bcolors.WARNING + "Input the number near your choice -> " + bcolors.OKGREEN)

    clear_console()
    appTitle()
    print(bcolors.WARNING + "--- [HOTKEY] ---" + bcolors.OKGREEN)
    print("")

    if choice == "1": 
        profile = 'kazuya'
        print("[NUM7] for PEWGF")
        print("[NUM9] for EWGF")

    elif choice == "2": 
        profile = 'heihachi'
        print("[NUM7] for OTGF")
        print("[NUM9] for EWGF")

    elif choice == "3": 
        profile = 'jin'
        print("[NUM9] for EWGF")

    elif choice == "4": 
        profile = 'dragunov'
        print("[NUM9] for iWR2")

    elif choice == "5": 
        profile = 'king'
        print("[NUM9] for iShiningWizard")

    elif choice == "6": 
        profile = 'generic'

    elif choice == "7": 
        exit()
    else: 
        exit()

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


menuStart()
