import time
import os

import Collision
import controller
import deleteline
import ledmatrixdrawer
import points

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

    score = 0
    collision = Collision.Collision_Dedektor()
    current_block_position = (5, 0)

    full_line_detector = deleteline.FullLineDetector()
    calculator = points.Points()

    game_over = False
    while not game_over:



        current_block = next_block
        score = calculator.points(score, 0, 1)
        next_block = rand.get_random_block()

        # Get Preview Block
        preview_block = next_block.strech_block_twice()

        # Prepare red_playgound to repaint...
        red_playground.clear()

        # Add preview block to red_playgound
        red_playground.add_block(preview_block, 0, 0)
        red_playground.add_block(numbertoblock.NumberToBlock.get_block(score), 10, 0)
        # draw red_playgound
        led_matrix_drawer.draw_playground(red_playground)

        # Spiel
        tim = 0.4
        countdown = 20
        rowcount = 0
        while countdown > 0:
            time.sleep(tim)
            countdown = countdown - 1

            linecount = 19 - countdown

            if score >= 50:
                tim = 0.35

            if score >= 100:
                tim = 0.3

            if score >= 200:
                tim = 0.28

            if score >= 300:
                tim = 0.26

            if score >= 400:
                tim = 0.24

            if score >= 500:
                tim = 0.20

            if score >= 1000:
                tim = 0.15

            if score >= 5000:
                tim = 5

            if collision.at_wall(color_playground, current_block,
                                          current_block_position[0]) == True:
                color_playground.add_block(current_block, current_block_position[0] - 1, current_block_position[1])
                rgg_led_drawer.draw_playground(color_playground)

                if collision.on_ground(color_playground, current_block,
                                                               current_block_position[1] + 1) == True:
                    countdown = 0
                    lines = full_line_detector.detect_lines(color_playground)
                    full_line_detector.delete_full_lines(lines, color_playground)
                    score = calculator.points(score, len(lines), 0)
                    break
                color_playground.block_clear(current_block, current_block_position[0] - 1, current_block_position[1])

                if current_block_position == "End!":
                    game_over = True

                if collision.with_block(color_playground, current_block, current_block_position[0],
                                                current_block_position[1] + 1) == True:
                    color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
                    rgg_led_drawer.draw_playground(color_playground)
                    lines = full_line_detector.detect_lines(color_playground)
                    full_line_detector.delete_full_lines(lines, color_playground)
                    score = calculator.points(score, len(lines), 0)
                    break
                current_block_position = (current_block_position[0] - 1, current_block_position[1] )


            color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
            rgg_led_drawer.draw_playground(color_playground)

            if collision.on_ground(color_playground, current_block,
                                                           current_block_position[1]+1) == True:
                countdown = 0
                lines = full_line_detector.detect_lines(color_playground)
                full_line_detector.delete_full_lines(lines, color_playground)
                score = calculator.points(score, len(lines), 0)
                break

            color_playground.block_clear(current_block, current_block_position[0], current_block_position[1])

            current_block_position = gamepad.get_button_pressed(current_block, current_block_position)
            if current_block_position == "End!":
                game_over = True

            if collision.with_block(color_playground, current_block, current_block_position[0],
                                            current_block_position[1] + 1) == True:
                color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
                rgg_led_drawer.draw_playground(color_playground)
                lines = full_line_detector.detect_lines(color_playground)
                full_line_detector.delete_full_lines(lines, color_playground)
                score = calculator.points(score, len(lines), 0)
                break

            current_block_position = (current_block_position[0], current_block_position[1] + 1)

        current_block_position = (color_playground.width // 2, 0)


pygame.mixer.init()

Name = './Music/Tetris Edit 1 Export 3.mp3'

pygame.mixer.music.load(Name)

pygame.mixer.music.play(-1)

if __name__ == "__main__":
    run_game()
