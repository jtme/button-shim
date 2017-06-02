#!/usr/bin/env python

import signal
import buttonshim
import sys

try:
    from evdev import uinput, UInput, ecodes as e
except ImportError:
    exit("This library requires the evdev module\nInstall with: sudo pip install evdev")

KEYCODES = [e.KEY_A, e.KEY_B, e.KEY_C, e.KEY_D, e.KEY_E]

print("""
Button SHIM: keyboard.py

Control the audio volume on your Raspberry Pi!

Press Ctrl+C to exit.

""")

try:
    ui = UInput({e.EV_KEY: KEYCODES}, name="Button-SHIM", bustype=e.BUS_USB)

except uinput.UInputError as e:
    sys.stdout.write(e.message)
    sys.stdout.write("Have you tried running as root? sudo {}".format(sys.argv[0]))
    sys.exit(0)


@buttonshim.on_press([buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E])
def button_p_handler(button, pressed):
    keycode = KEYCODES[button]
    print("Press: {}".format(keycode))
    ui.write(e.EV_KEY, keycode, 1)
    ui.syn()

@buttonshim.on_release([buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E])
def button_r_handler(button, pressed):
    keycode = KEYCODES[button]
    print("Release: {}".format(keycode))
    ui.write(e.EV_KEY, keycode, 0)
    ui.syn()

signal.pause()
