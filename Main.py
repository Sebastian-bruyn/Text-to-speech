from gtts import gTTS
import os
from playsound import playsound


#Text Input
Text = input()

#Conversion
TextSound= gTTS(Text)

#File management
os.remove('text.mp3')
TextSound.save('text.mp3')

#text output
playsound('text.mp3')