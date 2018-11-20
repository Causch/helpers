#!/usr/bin/python
import struct
import time
import sys
import os
from threading import Timer

def screenoff():
  os.system("echo 1 > /sys/class/backlight/rpi_backlight/bl_power")

infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

t=Timer(30.0, screenoff)

#open file in binary mode
in_file = open(infile_path, "rb")

os.system("echo 1 > /sys/class/backlight/rpi_backlight/bl_power")

t.start()
event = in_file.read(EVENT_SIZE)
t.cancel()
os.system("echo 0 > /sys/class/backlight/rpi_backlight/bl_power");

while event:
    t=Timer(30.0, screenoff)
    t.start()
    event = in_file.read(EVENT_SIZE)
    t.cancel()
    os.system("echo 0 > /sys/class/backlight/rpi_backlight/bl_power")
in_file.close()



