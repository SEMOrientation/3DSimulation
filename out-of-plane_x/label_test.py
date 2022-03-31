#!/usr/bin/env python3
import os
import math
import random

EXAMPLES_PER_ROTATION = 5
INTERVAL = 5.0

for f in os.listdir():
    name, ext = os.path.splitext(f)
    if ext.lower() != ".png":
        continue

    frame = int(name)
    # seed random and get the angle
    random.seed(frame)
    angle = math.degrees(random.random()*2*math.pi)

    # properly format new filename and rename
    name_ = f"{frame:04}_{angle:06.2f}"
    os.rename(f, name_+ext)
