#!/usr/bin/env python3
import os
import math

EXAMPLES_PER_ROTATION = 5
INTERVAL = 15.0

def get_angle(frame, examples, interval):
    ax1_rot = math.floor(frame/examples)*interval
    return (ax1_rot%360,
            math.floor(ax1_rot/360)*interval)

for f in os.listdir():
    name, ext = os.path.splitext(f)
    if ext.lower() != ".png":
        continue

    frame = int(name)
    # convert frame number to angle and index
    anglex, angley = get_angle(frame, EXAMPLES_PER_ROTATION, INTERVAL)
    number = frame % EXAMPLES_PER_ROTATION

    # properly format new filename and rename
    name_ = f"{number:02}_{anglex:06.2f}_{angley:06.2f}"
    os.rename(f, name_+ext)
