# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:45:11 2019

@author: Mårten Karlberg
"""

import functions
import constant
from pathlib import Path

input_file = "data/iowords.orc"
midi_output_file = "data/iowords.mid"

path = Path(input_file)
print(path.stat().st_size / 1024, "kB")

with open(input_file, "rb") as orc_file: 
    # MIDI
    # 1. read riff header ckID = RIFF (chID = A four-character code that identifies the representation of the chunk data data. A program reading a RIFF file can skip over any chunk whose chunk ID it doesnt recognize; it simply skips the number of bytes specified by ckSize plus the pad byte, if present.)
    # 2. read ckSize (A 32-bit unsigned value identifying the size of ckData. This size value does not include the size of the ckID or ckSize fields or the pad byte at the end of ckData.)
    # 3. write ckData to new midi file, (ckData = Binary data of fixed or variable size. The start of ckData is word-aligned with respect to the start of the RIFF file. If the chunk size is an odd number of bytes, a pad byte with value zero is written after ckData. Word aligning improves access speed (for chunks resident in memory) and maintains compatibility with EA IFF. The ckSize value does not include the pad byte.)
    # source: http://www.tactilemedia.com/info/MCI_Control_Info.html

    functions.check_riff_header(orc_file, constant.RIFF_HEADER_START)
    midi_data_size = functions.check_riff_header(orc_file, constant.RIFF_HEADER_MIDI)
    midi = orc_file.read(midi_data_size)

    with open(midi_output_file, "wb") as midi_file:
        num_bytes_written = midi_file.write(midi)
        print(num_bytes_written)

    # WAVE
    # 1. read riff header
    # 2. try and understand how wave chuck should be split to different channels
    # 3. write channels to individual wav-files
    # 4. how handle metadata, eg. pan and volume?

    # wave_data_size = functions.check_riff_header(orc_file)
