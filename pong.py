import objects
import ledmatrixdrawer
import playground
import points
# import random_blocks
import rgbleddrawer
import controller
import pygame
import numbertoblock
import datetime
import Collision
import gamespeed
import time
import random
from controller import Controller
from Ball_Steuerung import Ball_Steuerung


def show_clock_until_start_is_pressed(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer, controller):
    while True:
        color_playground.clear()
        red_playground.clear()
        # TODO: this is a quite ugly hack, since NumberToBlock only supports 4 digit numbers
        now = datetime.datetime.now()
        min = now.time().minute
        hour = now.time().hour
        mon = now.date().month
        today = now.date().day
        sec = now.time().second
        year = now.date().year % 100
        color_playground.add_block(numbertoblock.NumberToBlock.get_block(hour * 100), 0, 0)
        color_playground.add_block(numbertoblock.NumberToBlock.get_block(min * 100), 0, 6)
        color_playground.add_block(numbertoblock.NumberToBlock.get_block(sec * 100), 0, 12)
        red_playground.add_block(numbertoblock.NumberToBlock.get_block(today * 100 + mon), 0, 0)
        red_playground.add_block(numbertoblock.NumberToBlock.get_block(year * 100), 21, 0)

        rgg_led_drawer.draw_playground(color_playground)
        led_matrix_drawer.draw_playground(red_playground)
        pygame.time.Clock().tick(1)

        # rand = random_blocks.Randomblock()
        # next_block = rand.get_random_block()
        result = controller.get_button_pressed()
        if result == "Restart":
            break
    color_playground.clear()
    red_playground.clear()


def run_game():
    # variables for objects
    paddle_left = objects.object_list[0]
    paddle_right = objects.object_list[1]
    paddle_top = objects.object_list[2]
    paddle_bot = objects.object_list[3]
    ball = objects.object_list[4]
    loser1 = False
    loser2 = False

    anfang = random.random()
    # Some stuff needed by PyGame
    pygame.init()

    # use Joystick and Controller
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    gamepad = controller.Controller(joystick)

    # drawer for playfield
    rgb_led_drawer = rgbleddrawer.RgbLedDrawer()

    # drawer for scoreboard
    led_matrix_drawer = ledmatrixdrawer.LedMatrixDrawer()

    # Playgrounds
    color_playground = playground.Playground(20, 10)
    red_playground = playground.Playground(8, 32)

    show_clock_until_start_is_pressed(color_playground, rgb_led_drawer, red_playground, led_matrix_drawer, gamepad)

    color_playground.add_object(paddle_top, 4, 0)
    color_playground.add_object(paddle_bot, 4, 17)
    if anfang > 0.5:
        color_playground.add_object(ball, 5, 3)
    else:
        color_playground.add_object(ball, 5, 14)
    # draw red_playgound
    rgb_led_drawer.draw_playground(color_playground)
    # Spiel
    pygame.time.wait(5000)
    del led_matrix_drawer
    del rgb_led_drawer
    pygame.event.get()
    pygame.quit()


def block_is_above_beginning(block, line):
    for y in range(block.height):
        for x in range(block.width):
            if block.get_field()[y][x] == 1:
                if y + line <= 0:
                    return True
    return False


def block_is_below_beginning(block, line):
    for y in range(block.height):
        for x in range(block.width):
            if block.get_field()[y][x] == 1:
                if y + line > 20:
                    return True
    return False


def check_for_full_lines(calculator, color_playground, full_line_detector, score):
    lines = full_line_detector.detect_lines(color_playground)
    full_line_detector.delete_full_lines(lines, color_playground)
    score = calculator.points(score, len(lines), 0)
    return score


def round(b: object, b1: object, b2: object, c: Collision.Collision_Dedektor, p: playground, bs: Ball_Steuerung, joy1,
          joy2):
    Ball_Steuerung.position_calculator(bs, p, b1, b2, c, b)
    Controller.Paddle_Steuerung(joy1, b1)
    Controller.Paddle_Steuerung(joy2, b2)


if __name__ == "__main__":
    while True:
        run_game()
