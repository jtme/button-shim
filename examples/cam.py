#!/usr/bin/env python

import signal
import buttonshim

print("""
Button SHIM: rainbow.py

Command on button press. 

Press Ctrl+C to exit.

""")

import commands
    
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    buttonshim.set_pixel(0x94, 0x00, 0xd3)  
    s=commands.getstatusoutput("raspistill -w 320 -h 240 -o IMG/snap.jpg")
    print s
    
    if s[0] != 0:
                self.output(s[1], s[0])
      else:
                self.output("error occured", status[0])
            
            

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    buttonshim.set_pixel(0x00, 0x00, 0xff)


@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    buttonshim.set_pixel(0x00, 0xff, 0x00)


@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    buttonshim.set_pixel(0xff, 0xff, 0x00)


@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)


signal.pause()
