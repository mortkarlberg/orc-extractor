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

def extract_data_chunk(in_file, out_file, data_size, pad_bytes = 0):
    data = in_file.read(data_size)

    with open(out_file, "wb") as out:
        num_bytes_written = out.write(data)
        print(num_bytes_written)

    if pad_bytes:
        in_file.read(pad_bytes)
