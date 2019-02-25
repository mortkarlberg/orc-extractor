# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:08:16 2019

@author: Mårten
"""

def check_riff_header(file, header_name):
    header_bytes = file.read(len(header_name))
    print(bytes)
    if header_name != header_bytes:
        print("Unknown file content.", header_bytes)
        exit()

    size_bytes = file.read(4)
    size = int.from_bytes(size_bytes, "little")

    read_bytes = header_bytes + size_bytes
    print(size, read_bytes)

    return size, read_bytes

def extract_data_chunk(in_file, out_path, data_size, pad_bytes = 0):
    data = in_file.read(data_size)

    with out_path.open("wb") as out:
        num_bytes_written = out.write(data)
        print(num_bytes_written)

    if pad_bytes:
        in_file.read(pad_bytes)
