#!/usr/bin/env python3
import numpy as np
from PIL import Image
import os
import sys
import subprocess

def rerender(blend, frames):
    if isinstance(frames, list):
        frames = ",".join(frames)
    cwd = os.path.abspath(os.getcwd())
    if cwd[-1] != os.path.sep:
        cwd += os.path.sep
    os.chdir(os.path.expanduser("~"))
    cmd = ["bash", "-c", f"blender -b -y \"{blend}\" -y -o \"{cwd}\" -f \"{str(frames)}\""]
    popen = subprocess.Popen(cmd).wait()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("missing blend file")
    blend = os.path.expanduser(sys.argv[1])
    to_rerender = []
    for imf in os.listdir():
        name, ext = os.path.splitext(imf)
        if ext.lower() != ".png":
            continue
        im = np.array(Image.open(imf))
        if im.max() <= 10:
            print(imf)
            to_rerender.append(str(int(name)))
    rerender(blend, to_rerender)
