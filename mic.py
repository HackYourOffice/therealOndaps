#!/usr/bin/python
## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm for sound capture. Set
## various attributes of the capture, and reads in a loop,
## Then prints the volume.
##
## To test it out, run it and shout at your microphone:

import alsaaudio, audioop, os, configparser
from aiy.voice.audio import play_wav
from aiy.board import Board
from led import *



# Config block
print("Reading Config")
Config = configparser.ConfigParser()
Config.read("micpyconfig.ini")
config_noise_volume_threshold = int(Config.get('Noise', 'VolumeThreshold'))
config_noise_length_threshold = int(Config.get('Noise', 'LengthThreshold'))
config_sound = Config.get('Audio', 'Soundfile')
print("Configured sound file: " + config_sound)
print("Configuration finished")

print("Waiting for voice input...")

# Open the device in nonblocking capture mode. The last argument could
# just as well have been zero for blocking mode. Then we could have
# left out the sleep call in the bottom of the loop
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

# The period size controls the internal number of frames per period.
# The significance of this parameter is documented in the ALSA api.
# For our purposes, it is sufficient to know that reads from the device
# will return this many frames. Each frame being 2 bytes long.
# This means that the reads below will return either 320 bytes of data
# or 0 bytes of data. The latter is possible because we are in nonblocking
# mode.
inp.setperiodsize(800)
board = Board()
led_blink(board, 0.5, 2)
counter = 0
while True:
        # Read data from device
        l,data = inp.read()
        if l:
            # Return the maximum of the absolute value of all samples in a fragment.
            if audioop.max(data, 2) > config_noise_volume_threshold:
                counter += 1
                if counter >= config_noise_length_threshold * 10:
                    counter /= 2
                    led_on(board)
                    play_wav(os.path.expanduser(config_sound))
                    led_off(board)
                    while l:
                       l,data = inp.read()
            else:
                if counter > 0:
                    counter -= 1
        time.sleep(.001)
