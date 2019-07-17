import time

from luma.led_matrix.device import neopixel

import random_blocks
import playground
import pygame
import drawer
import tetris_blocks

pygame.init()
pygame.joystick.init()
a = pygame.joystick.Joystick(0)
a.init()

device = neopixel(width=10, height=20, rotate=0, mapping=drawer.HAT)

play = playground.Playground(20, 10)
play.draw()


rand = random_blocks.Randomblock()
blo = rand.get_random_block()

Drawer1 = drawer.draw(device)

blo.draw_block()
Drawer1.draw_playground(play)

play.add_block(blo)
Drawer1.device

device.clear()
Drawer1.draw_playground(play)



time.sleep(10)