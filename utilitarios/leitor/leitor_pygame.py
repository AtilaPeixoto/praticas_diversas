from gtts import gTTS
import pygame
from time import sleep


som = 'audio.mp3'
s = gTTS(text='este funciona bem', lang='pt-br')
s.save(som)


pygame.init()
pygame.mixer.init()


pygame.mixer.music.load(som)
sleep(2)
pygame.mixer.music.play()


while pygame.mixer.music.get_busy():
    pygame.time.delay(100)