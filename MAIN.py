#!/usr/bin/python3
import pygame
import pong
import tetris
import Glock
import controller

pygame.init()
pygame.fastevent.init()
x = 0
joystick = pygame.joystick.Joystick(0)
gamepad = controller.Controller(joystick)
if gamepad.get_button_pressed() == "Right Title":
    x +=1
if gamepad.get_button_pressed() == "Left Title":
    x-=1
if x <= 0:
    x = 2
if x >= 2:
    x = 0

if x == 0:
    tetris.run_game()
if x == 1:
    Glock.run_game()
if x == 2:
    pong.run_game()
pygame.quit()
quit()
