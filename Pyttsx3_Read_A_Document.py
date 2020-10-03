import pyttsx3
from pyttsx3 import engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
filename = ["RobertFrostRoadNotTaken.txt"]#Put file name here
b=[]
zira = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" #Microsoft David
david = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"#Microsoft Zira
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+-20)#Change speaking speed
for files in filename:
    f=open(files,'r')#Open in read mode
    contents=f.read()
    contents=contents.split('\n')
    b.append(contents[-1])
    f.close()#Close file
count1=0
for element in b:
    count1=count1+1
    if b.count(element)>1:
        print(element)
        print(filename[count1-1])
for voice in voices:
    engine.setProperty('voice', zira)#Choose voice
    engine.say(contents)
engine.runAndWait()



