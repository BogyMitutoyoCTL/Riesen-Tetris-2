import time

import Collision
import controller
import ledmatrixdrawer

import random_blocks
import playground
import pygame
import drawer
import deleteline
import rgbleddrawer

from Colors import Block_color
from numers_for_score import Numbers
from tetris_blocks import Block


def draw_digit(i, posx, posy, red_playground, red_drawer):
    digit = Numbers.number[i]
    rotatable = [digit] * 4
    b = Block(rotatable, Block_color.red)
    red_playground.add_block(b, posx, posy)
    red_drawer.draw_playground(red_playground)


def draw_number(t, red_playground, red_drawer):
    erste_nummer = t % 10
    intermediate = t // 10
    zweite_nummer = intermediate % 10
    intermediate = intermediate // 10
    dritte_nummer = intermediate % 10
    intermediate = intermediate // 10
    vierte_nummer = intermediate % 10
    draw_digit(vierte_nummer % 10, 10, 0, red_playground, red_drawer)
    draw_digit(dritte_nummer % 10, 15, 0, red_playground, red_drawer)
    draw_digit(zweite_nummer % 10, 20, 0, red_playground, red_drawer)
    draw_digit(erste_nummer % 10, 25, 0, red_playground, red_drawer)


def run_game():
    # Some stuff needed by PyGame
    pygame.init()

    # use Joystick and Controller
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    gamepad = controller.Controller(joystick)

    # drawer for playfield
    rgg_led_drawer = rgbleddrawer.RgbLedDrawer()

    # drawer for scoreboard
    led_matrix_drawer = ledmatrixdrawer.LedMatrixDrawer()

    # Playgrounds
    color_playground = playground.Playground(20, 10)
    red_playground = playground.Playground(8, 32)

    # Random block generator and first random block
    rand = random_blocks.Randomblock()
    next_block = rand.get_random_block()

    t = 0
    fadfaf = Collision.Collision_Dedektor()
    current_block_position = (5, 0)

    game_over = False
    while not game_over:

        current_block = next_block
        next_block = rand.get_random_block()

        # Get Preview Block
        preview_block = next_block.strech_block_twice()

        # Prepare red_playgound to repaint...
        red_playground.clear()

        # Add preview block to red_playgound
        red_playground.add_block(preview_block, 0, 0)

        #draw red_playgound
        led_matrix_drawer.draw_playground(red_playground)

        draw_number(t, red_playground, led_matrix_drawer)

        # Spiel
        tim = 0.5
        countdown = 20
        rowcount = 0
        while countdown > 0:
            time.sleep(tim)
            countdown = countdown - 1

            linecount = 19 - countdown

            if t >= 50:
                tim = 0.4

            if t >= 100:
                tim = 0.3

            if t >= 200:
                tim = 0.28

            if t >= 300:
                tim = 0.26

            if t >= 400:
                tim = 0.24

            if t >= 500:
                tim = 0.20

            if t >= 1000:
                tim = 0.15

            if t >= 5000:
                tim = 0.1

            if fadfaf.collision(color_playground, current_block, 0, linecount) == True:
                countdown = 0

            color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
            rgg_led_drawer.draw_playground(color_playground)
            color_playground.block_clear(current_block, current_block_position[0], current_block_position[1])

            current_block_position = gamepad.get_button_pressed(current_block, current_block_position)
            if current_block_position == "End!":
                game_over = True

            current_block_position = (current_block_position[0], current_block_position[1] + 1)

        t = t + 1
        current_block_position = (current_block_position[0], current_block_position[1] - 20)
    # bis hier in die schleife dann...


if __name__ == "__main__":
    run_game()
