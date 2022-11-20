from pynput.keyboard import Listener as KeyboardListener
import subprocess as s

trigger = 'x'
counter = 0

def on_press(key):
    global trigger, counter
    try:
        if key.char == trigger:
            if counter == 0:
                process = s.Popen(['python','get_text.py'])
            counter += 1
    except AttributeError:
        pass

def on_release(key):
    global trigger, counter
    try:
        if key.char == trigger:
            counter = 0
    except AttributeError:
        pass

with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
    listener.join()