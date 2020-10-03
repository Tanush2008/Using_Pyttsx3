import pyttsx3
from pyttsx3 import engine
engine = pyttsx3.init()
ml_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
fm_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', fm_voice)
engine.say('Hello, I am Microsoft Zira')
engine.setProperty('voice', ml_voice)
engine.say('Hello I am Microsoft David')
engine.runAndWait()
