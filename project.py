from gtts import gTTS

import os

f=open('project.txt')
x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("project.wav")
os.system("project.wav")
