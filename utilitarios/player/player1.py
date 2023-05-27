import pygame


lista = 'player\\musica-audio\\cbj.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(lista)
                        
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
# pygame.event.wait()


while pygame.mixer.music.get_busy():
    pygame.time.delay(100)