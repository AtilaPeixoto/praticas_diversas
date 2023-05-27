from gtts import gTTS
from playsound import *
from time import sleep

som = 'audio.mp3'
falar = 'aqui falar falar3'

s = gTTS(text=falar, lang='pt-br')
s.save(som)

sleep(2)
playsound(som)








