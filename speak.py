'''
Sample python script to demonstrate TTS using pyttsx3
'''
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 120)

engine.setProperty('voice', 'en+f3')
engine.say("Welcome World")

engine.runAndWait()
