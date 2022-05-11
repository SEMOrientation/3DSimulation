#!/usr/bin/env python3
import os
import math
import random

EXAMPLES_PER_ROTATION = 5
INTERVAL = 30.0

def rand_angle(seed):
    """Returns a random angle [0, 2pi) for a given seed."""
    random.seed(seed)
    return random.random()*2*math.pi, random.random()*2*math.pi

for f in os.listdir():
    name, ext = os.path.splitext(f)
    if ext.lower() != ".png":
        continue

    frame = int(name)
    anglex, angley = rand_angle(frame)
    anglex = math.degrees(anglex)
    anglex = round(anglex, 2)
    angley = math.degrees(angley)
    angley = round(angley, 2)

    while anglex >= 360:
        anglex -= 360
    while angley >= 360:
        angley -= 360

    # properly format new filename and rename
    name_ = f"{frame:05}_{anglex:06.2f}_{angley:06.2f}"
    os.rename(f, name_+ext)
