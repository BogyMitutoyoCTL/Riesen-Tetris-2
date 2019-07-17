import controller
import tetris_blocks
import Colors
import drawer
import highscorelist
import littlemonitor
import points
import random_blocks
import playground
import pygame
import littlemonitor

a = pygame.joystick.Joystick(0)
a.init()

play = playground.Playground(20, 10)
play.draw()