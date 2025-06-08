# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:27:53 2019

@author: naz xzawiz
"""

from gtts import gTTS
import os
tts = gTTS(text='Hii', lang='en')
tts.save("C:/Users/naz xzawiz/.spyder-py3/Picamera/audio.mp3")
os.system("mpg321 C:/Users/naz xzawiz/.spyder-py3/Picamera/audio.mp3")


