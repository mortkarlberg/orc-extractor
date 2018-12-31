# orc-extractor
Extract wave, midi and other data from orc-files (Voyetra Digital Orchestrator)

### File Description
All ORC files have the same format as RMI, but with some differences:
* ORC files don't use DLS sample banks.
* There is only one WAV track with all digital audio samples.
* Sample playback is controlled by Sequencer-Specific events in the MIDI sequence and by "voyl" chunk in the WAV track.

### RIFF Tree Structure
~~~
File Root
│
├─ RIFF:RMID     - RIFF MIDI header
│  └─ data       - MIDI data chunk
│
└─ RIFF:WAVE     - RIFF Wave header
   ├─ fmt        - Wave format chunk
   ├─ voyl       - Voyetra special chunk
   └─ data       - Waveform data chunk
~~~

### Resources
http://www.vgmpf.com/Wiki/index.php?title=ORC
http://www.vgmpf.com/Wiki/index.php?title=RMI
