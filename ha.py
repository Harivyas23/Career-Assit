# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:23:04 2019

@author: naz xzawiz
"""

import os
import subprocess
from subprocess import call

cmd_beg= 'espeak '
cmd_end= ' | aplay /C:/Users/naz xzawiz/.spyder-py3/Picamera/example.mp3  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out= '--stdout > /C:/Users/naz xzawiz/.spyder-py3/Picamera/example.mp3 ' # To store the voice file


str = ('/C:/Users/naz xzawiz/.spyder-py3/Picamera/havy.txt')
str.replace(' ', '_')

call([cmd_beg+cmd_out+str+cmd_end], shell=True)

os.system("aplay /C:/Users/naz xzawiz/.spyder-py3/Picamera/example.mp3")