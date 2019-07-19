import pygame
import time


pygame.mixer.init()
Name = '/home/pi/Downloads/Tetris.mp3'

pygame.mixer.music.load(Name)
i = 0

pygame.mixer.music.play(0)