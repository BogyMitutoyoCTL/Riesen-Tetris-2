import time
import pygame
import datetime

import Collision
import controller
import deleteline
import gamespeed
import ledmatrixdrawer
import numbertoblock
import playground
import points
import random_blocks
import rgbleddrawer
def titlescreen(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer, controller):
    #todo hier kommt die allgemeine titlescreen methode hin, in der ausgesucht wird welcher angezeigt wird usw
    clock_titlescreen(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer, controller)
def clock_titlescreen(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer, controller):
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

        rand = random_blocks.Randomblock()
        next_block = rand.get_random_block()
        result = controller.get_button_pressed(next_block, (1, 1), Collision.Collision_Dedektor(),
                                               playground.Playground(20, 10))
        if result == "Restart":
            break
    color_playground.clear()
    red_playground.clear()