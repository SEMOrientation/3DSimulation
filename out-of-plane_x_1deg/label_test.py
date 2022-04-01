#!/usr/bin/env python3
import os
import math
import random

EXAMPLES_PER_ROTATION = 5
INTERVAL = 1.0

def rand_angle(seed):
    """Returns a random angle [0, 2pi) for a given seed."""
    random.seed(seed)
    return random.random()*2*math.pi

for f in os.listdir():
    name, ext = os.path.splitext(f)
    if ext.lower() != ".png":
        continue

    frame = int(name)
    angle = math.degrees(rand_angle(frame))

    # properly format new filename and rename
    name_ = f"{frame:04}_{angle:06.2f}"
    os.rename(f, name_+ext)
