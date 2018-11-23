# ondaps

Office noise detection and prevention system

## Prerequisites

* Google AIY VoiceKit
https://aiyprojects.withgoogle.com/voice/
https://www.pollin.de/p/google-aiy-voice-kit-fuer-raspberry-pi-3-b-810883
* Raspberry Pi
* MicroSD card

## Step by Step

* flash image to SD card TODO link
* sudo nmap -sP 10.0.10.0/22 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'

## Setup as systemd service
* you'll need to set up pulseaudio as a systemwide service -> https://possiblelossofprecision.net/?p=1956
* the user pi needs to have access to audio and gpio
* `sudo usermod -a -G audio,pulse,pulse-access,gpio pi`
