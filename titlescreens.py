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
import Ball_Steuerung
import titlescreens
import pong

def show_clock_until_start_is_pressed(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer,
                                      controller):
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
        if result == "Left Title":
            pong.run_game().pongtitlescreen = True
            pong.run_game().clock = False
        if result == "Right Title":
            pong.run_game().tetristitlescreen = True
            pong.run_game().clock = False
    color_playground.clear()
    red_playground.clear()
def show_pong_titlescreen(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer,controller):
    while True:
        color_playground.clear()
        red_playground.clear()
        # TODO: this is a quite ugly hack, since NumberToBlock only supports 4 digit numbers
        now = datetime.datetime.now()
        sec = now.time().minute
        hour = now.time().hour
        mon = now.date().month
        today = now.date().day
        min = now.time().second
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
        if result == "Left Title":
            pong.run_game().tetristitlescreen = True
            pong.run_game().pongtitlescreen = False
        if result == "Right Title":
            pong.run_game().clock = True
            pong.run_game().pongtitlescreen = False
        if result == "Restart":
            pong.run_game().pongplay = True
            pong.run_game().pongtitlescreen = False
    color_playground.clear()
    red_playground.clear()
def show_tetris_titlescreen(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer, controller):
    while True:
        color_playground.clear()
        red_playground.clear()
        # TODO: this is a quite ugly hack, since NumberToBlock only supports 4 digit numbers
        now = datetime.datetime.now()
        min = now.time().minute
        sec = now.time().hour
        mon = now.date().month
        today = now.date().day
        hour = now.time().second
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
        if result == "Left Title":
            pong.run_game().clock = True
            pong.run_game().tetristitlescreen = False
        if result == "Right Title":
            pong.run_game().pongtitlescreen = True
            pong.run_game().tetristitlescreen = False
        if result == "Restart":
            pong.run_game().tetrisplay = True
            pong.run_game().tetristitlescreen = False
    color_playground.clear()
    red_playground.clear()