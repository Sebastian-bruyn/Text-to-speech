import pyttsx3

engine = pyttsx3.init()

#input
Text = input()

#Output
engine.say(Text)
engine.runAndWait()