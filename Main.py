from gtts import gTTS
import os
from playsound import playsound



Text = input()
TextSound= gTTS(Text)
os.remove('text.mp3')
TextSound.save('text.mp3')
playsound('text.mp3')