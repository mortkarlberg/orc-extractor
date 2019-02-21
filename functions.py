# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:08:16 2019

@author: Mårten
"""

import constant

def check_riff_header(file):
    bytes = file.read(4)
    print(bytes)
    if constant.RIFF_HEADER_START != bytes:
        print("Unknown file content.")
        exit()

    bytes = file.read(4)
    ckSize = int.from_bytes(bytes, "little")
    print(ckSize)

    return ckSize
