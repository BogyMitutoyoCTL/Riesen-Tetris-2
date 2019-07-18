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


def draw_number(i, posx, posy):
    digit = Numbers.number[i]
    rotatable = [digit] * 4
    b = Block(rotatable, Block_color.red)
    red_playground.add_block(b, posx, posy)
    red_drawer.draw_playground(red_playground)

# Some stuff needed by PyGame
pygame.init()

# use Joystick and Controller
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
gamepad = controller.Controller(joystick)

# drawer for playfield
color_canvas = neopixel(width=10, height=20, rotate=0, mapping=drawer.HAT)
color_drawer = drawer.draw(color_canvas)

# drawer for scoreboard
serial = spi(port=0, device=0, gpio=noop())
red_canvas = max7219(serial, cascaded=4, block_orientation=90,
                     rotate=0, blocks_arranged_in_reverse_order=True)
red_drawer = littlemonitor.draw_small(red_canvas)

# Playgrounds
color_playground = playground.Playground(20, 10)

red_playground = playground.Playground(8, 32)

# Random block generator and first random block
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

fadfaf = Collision.Collision_Dedektor()
current_block_position = (5, 0)

game_over = False
while not game_over:

    current_block = next_block
    next_block = rand.get_random_block()

    next_block = rand.get_random_block()

    # Vorschau
    preview_block = next_block.strech_block_twice()
    red_playground.clear()
    red_playground.add_block(preview_block, 0, 0)
    red_drawer.draw_playground(red_playground)

    erste_nummer = t % 10
    intermediate = t // 10
    zweite_nummer = intermediate % 10
    intermediate = intermediate // 10
    dritte_nummer = intermediate % 10
    intermediate = intermediate // 10
    vierte_nummer = intermediate % 10
    draw_number(vierte_nummer % 10, 10, 0)
    draw_number(dritte_nummer % 10, 15, 0)
    draw_number(zweite_nummer % 10, 20, 0)
    draw_number(erste_nummer % 10, 25, 0)


    # Spiel
    tim = 0.5
    countdown = 20
    rowcount = 0
    while countdown > 0:
        time.sleep(tim)
        countdown = countdown - 1

        linecount = 19 - countdown

        if erste_nummer == 5:
            tim = 0.4

        if zweite_nummer == 1:
            tim = 0.3

        if zweite_nummer == 2:
            tim = 0.28

        if zweite_nummer == 3:
            tim = 0.26

        if zweite_nummer == 4:
            tim = 0.24

        if zweite_nummer == 5:
            tim = 0.20

        if dritte_nummer == 1:
            tim = 0.15

        if dritte_nummer == 5:
            tim = 0.1

        if vierte_nummer == 1:
            tim = 0.05

        if fadfaf.collision(color_playground, current_block, 0, linecount) == True:
            pass

        color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
        color_playground.add_block(current_block, rowcount, linecount)

        color_playground.add_block(current_block, 0, linecount)

        color_drawer.draw_playground(color_playground)

        color_playground.block_clear(current_block, rowcount, linecount)

        action = gamepad.get_button_pressed(current_block, current_block_position)
        if action == "End!":
            game_over = True

        current_block_position = (current_block_position[0], current_block_position[1] + 1)


    t = t + 1
# bis hier in die schleife dann...
