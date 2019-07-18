import time

import Collision
import controller
import ledmatrixdrawer

import random_blocks
import playground
import pygame
import numbertoblock
import rgbleddrawer


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
        red_playground.add_block(numbertoblock.NumberToBlock.get_block(t) * 4, 10, 0)
        #draw red_playgound
        led_matrix_drawer.draw_playground(red_playground)

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





            if fadfaf.check_if_block_at_wall_right(color_playground, current_block, current_block_position[0]) == True:
                break

            #if fadfaf.check_if_block_at_wall_left(color_playground, current_block, current_block_position[0]) == True:
                #break

            color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
            rgg_led_drawer.draw_playground(color_playground)





            if fadfaf.check_if_block_on_ground(color_playground, current_block, current_block_position[1]+1) == True:
                countdown = 0
                break

            color_playground.block_clear(current_block, current_block_position[0], current_block_position[1])

            current_block_position = gamepad.get_button_pressed(current_block, current_block_position)
            if current_block_position == "End!":
                game_over = True

            if fadfaf.collision(color_playground, current_block, current_block_position[0], current_block_position[1]+1) == True:
                color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
                rgg_led_drawer.draw_playground(color_playground)
                break

            current_block_position = (current_block_position[0], current_block_position[1] + 1)





        current_block_position = (5, 0)
        t = t + 1
    # bis hier in die schleife dann...


if __name__ == "__main__":
    run_game()
