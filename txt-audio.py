#import builtins libraries
from gtts import gTTS
import os
import pygame

#define text to be converted to audio
text = "This is a text to be converted to audio"

#initialize gTTS
tts = gTTS(text=text, lang = 'en')
tts.save("audio.mp3")

#declare pygame
pygame.mixer.init()

#upload and run audio.mp3
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play()

#waiting for playing audio
while pygame.mixer.music.get_busy():
    continue

#remove audio file
os.remove("audio.mp3")
