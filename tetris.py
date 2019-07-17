import time
import Block_rotater
from luma.core.interface.serial import spi, noop
import controller
import littlemonitor
from luma.led_matrix.device import neopixel, max7219

import random_blocks
import playground
import pygame
import drawer

rotater = Block_rotater.Rotater()

pygame.init()
pygame.joystick.init()
a = pygame.joystick.Joystick(0)
a.init()

g = controller.Controller(a)

dev = neopixel(width=10, height=20, rotate=0, mapping=drawer.HAT)

serial = spi(port=0, device=0, gpio=noop())
dev2 = max7219(serial, cascaded=4, block_orientation=90,
               rotate=0, blocks_arranged_in_reverse_order=True)

play = playground.Playground(20, 10)
play.draw()

play2 = playground.Playground(8, 32)
play2.draw()

rand = random_blocks.Randomblock()
blo = rand.get_random_block()
blo3 = rand.get_random_block()
blo2 = blo3.strech_block_twice()

Drawer1 = drawer.draw(dev)

blo.draw_block()
Drawer1.draw_playground(play)
Drawer2 = littlemonitor.draw_small(dev2)

play.add_block(blo, 4, 4)
play2.add_block(blo2, 0, 0)

dev2.clear()
dev.clear()
Drawer1.draw_playground(play)

Drawer2.draw_playground(play2)
time.sleep(3)
t = 0
#solange noch kein gameover ist
#wenn der block sich nicht mehr bewegen kann
while t < 1000:
    blo = blo3
    blo3 = rand.get_random_block()
    blo2 = blo3.strech_block_twice()

    Drawer1 = drawer.draw(dev)

    blo.draw_block()
    Drawer1.draw_playground(play)
    Drawer2 = littlemonitor.draw_small(dev2)

    play.add_block(blo, 4, 4)
    play2.add_block(blo2, 0, 0)

    dev2.clear()
    dev.clear()
    Drawer1.draw_playground(play)

    Drawer2.draw_playground(play2)
    time.sleep(3)
    t=t+1
#bis hier in die schleife dann...

i = 0

while  i<100:
    rotater.control(g, blo)
    play.add_block(blo, 4, 4)
    Drawer1.draw_playground(play)
    time.sleep(0.11)

time.sleep(10)
