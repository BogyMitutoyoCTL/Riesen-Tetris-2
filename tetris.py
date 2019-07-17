import time
import Block_rotater
from luma.core.interface.serial import spi, noop

import Collision
import controller
import littlemonitor
from luma.led_matrix.device import neopixel, max7219

import random_blocks
import playground
import pygame
import drawer

from Colors import Block_color
from numers_for_score import Numbers
from tetris_blocks import Block


def draw_number(i):
    digit = Numbers.number[i]
    rotatable = [digit] * 4
    b = Block(rotatable, Block_color.red)
    red_playground.add_block(b, 8, 0)
    red_drawer.draw_playground(red_playground)


rotater = Block_rotater.Rotater()

pygame.init()
pygame.joystick.init()
a = pygame.joystick.Joystick(0)
a.init()

g = controller.Controller(a)

color_canvas = neopixel(width=10, height=20, rotate=0, mapping=drawer.HAT)

serial = spi(port=0, device=0, gpio=noop())
red_canvas = max7219(serial, cascaded=4, block_orientation=90,
                     rotate=0, blocks_arranged_in_reverse_order=True)

color_playground = playground.Playground(20, 10)

red_playground = playground.Playground(8, 32)

rand = random_blocks.Randomblock()
current_block = rand.get_random_block()
next_block = rand.get_random_block()
preview_block = next_block.strech_block_twice()

color_drawer = drawer.draw(color_canvas)

# Drawer1.draw_playground(play)
red_drawer = littlemonitor.draw_small(red_canvas)

# play.add_block(blo, 4, 4)
# play2.add_block(blo2, 0, 0)

red_canvas.clear()
color_canvas.clear()
# Drawer1.draw_playground(play)

red_drawer.draw_playground(red_playground)
t = 0
hindernis = rand.get_random_block()
fadfaf = Collision.Collision_Dedektor()
# solange noch kein gameover ist
# wenn der block sich nicht mehr bewegen kann
while t < 1000:
    current_block = next_block
    next_block = rand.get_random_block()

    # Vorschau
    preview_block = next_block.strech_block_twice()
    red_playground.clear()
    red_playground.add_block(preview_block, 0, 0)
    red_drawer.draw_playground(red_playground)

    draw_number(t % 10)
    # Spiel
    tim = 0.15
    countdown = 20
    while countdown > 0:
        time.sleep(tim)
        countdown = countdown - 1

        linecount = 19 - countdown

        color_playground.add_block(hindernis, 0, 19)

        if fadfaf.collision(color_playground, current_block, 0, linecount) == True:
            print("Kollision")
            break

        color_playground.add_block(current_block, 0, linecount)

        color_drawer.draw_playground(color_playground)

        color_playground.clear()

        rotater.control(g, current_block)

    t = t + 1
# bis hier in die schleife dann...
