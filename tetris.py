import time

from luma.core.interface.serial import spi, noop

import littlemonitor
from luma.led_matrix.device import neopixel, max7219

import random_blocks
import playground
import pygame
import drawer
import tetris_blocks

pygame.init()
pygame.joystick.init()
a = pygame.joystick.Joystick(0)
a.init()

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

Drawer1 = drawer.draw(dev)

blo.draw_block()
Drawer1.draw_playground(play)
Drawer2 = littlemonitor.draw_small(dev2)

play.add_block(blo, 4, 4)
play2.add_block(blo, 4, 4)

dev2.clear()
dev.clear()
Drawer1.draw_playground(play)

Drawer2.draw_playground(play2)

time.sleep(10)