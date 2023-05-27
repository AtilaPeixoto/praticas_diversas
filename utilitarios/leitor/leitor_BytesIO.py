from io import BytesIO
from gtts import gTTS
import pygame as pg
from time import sleep

''' Usar BytesIO permite que você salve o áudio na memória sem precisar criar um arquivo no disco com o .save()'''


mp3 = BytesIO()
texto = gTTS('hello man ', lang='en')
texto.write_to_fp(mp3)
mp3.seek(0)


pg.init()
pg.mixer.init()

pg.mixer.music.load(mp3)
sleep(2)
pg.mixer.music.play()

while pg.mixer.music.get_busy():
    pg.time.delay(100)