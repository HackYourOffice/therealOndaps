# ondaps

Office noise detection and prevention system

## Prerequisites

* Google AIY VoiceKit
https://aiyprojects.withgoogle.com/voice/
https://www.pollin.de/p/google-aiy-voice-kit-fuer-raspberry-pi-3-b-810883
* Raspberry Pi
* MicroSD card

## Step by Step

* flash image to SD card. The image can be found on https://aiyprojects.withgoogle.com/voice-v1/#assembly-guide-1-get-the-voice-kit-sd-image
* sudo nmap -sP 10.0.10.0/22 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'

* As a base script we found a code sample to monitor the microphone input volume on https://ubuntuforums.org/showthread.php?t=500337&s=e6f196e35bd62002850c10a0af874e80&p=6505818#post6505818

## Setup as systemd service
* you'll need to set up pulseaudio as a systemwide service -> https://possiblelossofprecision.net/?p=1956
* the user pi needs to have access to audio and gpio
* `sudo usermod -a -G audio,pulse,pulse-access,gpio pi`
