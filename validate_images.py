#!/usr/bin/env python3
import numpy as np
from PIL import Image
import os

THRESHOLD = 10

for imf in os.listdir():
    if os.path.splitext(imf)[1].lower() != ".png":
        continue
    im = np.array(Image.open(imf))
    if im.max() <= THRESHOLD:
        print(imf)
