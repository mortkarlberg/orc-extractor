# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:08:16 2019

@author: Mårten
"""

def check_riff_header(file, header_name):
    bytes = file.read(len(header_name))
    print(bytes)
    if header_name != bytes:
        print("Unknown file content.")
        exit()

    bytes = file.read(4)
    ckSize = int.from_bytes(bytes, "little")
    print(ckSize)

    return ckSize
