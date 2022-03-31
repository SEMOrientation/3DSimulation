#!/usr/bin/env python3
import os
import math

EXAMPLES_PER_ROTATION = 5
INTERVAL = 5.0

for f in os.listdir():
    name, ext = os.path.splitext(f)
    if ext.lower() != ".png":
        continue

    frame = int(name)
    # convert frame number to angle and index
    angle = math.floor(frame/EXAMPLES_PER_ROTATION)*INTERVAL
    number = frame % EXAMPLES_PER_ROTATION

    # properly format new filename and rename
    name_ = f"{number:02}_{angle:06.2f}"
    os.rename(f, name_+ext)
