# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:45:11 2019

@author: Mårten Karlberg
"""

import functions
import constant
from pathlib import Path

in_orc = Path("data/iowords.orc")
out_midi = Path("data/iowords.mid")
out_wave_format = Path("data/iowords-wave-format.wow")
out_wave_data = Path("data/iowords-wave-data.wow")
out_wave_voyl = Path("data/iowords-wave-voyl.wow")

print(in_orc)
print(in_orc.stat().st_size / 1024, "kB")

with in_orc.open("rb") as orc_file: 
    # MIDI
    # 1. read riff header ckID = RIFF (chID = A four-character code that identifies the representation of the chunk data data. A program reading a RIFF file can skip over any chunk whose chunk ID it doesnt recognize; it simply skips the number of bytes specified by ckSize plus the pad byte, if present.)
    # 2. read ckSize (A 32-bit unsigned value identifying the size of ckData. This size value does not include the size of the ckID or ckSize fields or the pad byte at the end of ckData.)
    # 3. write ckData to new midi file, (ckData = Binary data of fixed or variable size. The start of ckData is word-aligned with respect to the start of the RIFF file. If the chunk size is an odd number of bytes, a pad byte with value zero is written after ckData. Word aligning improves access speed (for chunks resident in memory) and maintains compatibility with EA IFF. The ckSize value does not include the pad byte.)
    # source: http://www.tactilemedia.com/info/MCI_Control_Info.html

    print(" --- MIDI ---")

    riff_size = functions.check_riff_header(orc_file, constant.RIFF_HEADER_START)
    midi_size = functions.check_riff_header(orc_file, constant.RIFF_HEADER_MIDI)
    midi_pad_bytes = riff_size - midi_size - len(constant.RIFF_HEADER_MIDI) - constant.RIFF_HEADER_SIZE_BYTES
    print(midi_pad_bytes)

    functions.extract_data_chunk(orc_file, out_midi, midi_size, midi_pad_bytes)

    # WAVE
    # 1. extract each data chunk into three different files
    # 2. try and understand how wave chuck should be split to different channels
    # 3. write channels to individual wav-files
    # 4. how handle metadata, eg. pan and volume?

    print(" --- WAVE ---")

    wave_size = functions.check_riff_header(orc_file, constant.RIFF_HEADER_START)
    format_size = functions.check_riff_header(orc_file, constant.RIFF_HEADER_WAVE_START)
    functions.extract_data_chunk(orc_file, out_wave_format, format_size)

    voyl_size = functions.check_riff_header(orc_file, constant.RIFF_HEADER_WAVE_VOYL)
    functions.extract_data_chunk(orc_file, out_wave_voyl, voyl_size, voyl_size % 4)

    data_size = functions.check_riff_header(orc_file, constant.RIFF_HEADER_WAVE_DATA)
    functions.extract_data_chunk(orc_file, out_wave_data, data_size)

    print("Successfully extracted", in_orc)