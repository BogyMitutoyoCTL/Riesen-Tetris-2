import pygame
import time


pygame.mixer.init()
Name = '/home/pi/Downloads/Tetris.mp3'
Name2 = '/home/pi/Downloads/jump_01.wav'

jump = pygame.mixer.Sound(Name2)
pygame.mixer.music.load(Name)
i = 0

pygame.mixer.music.play(0)