import object_playground
import rgbleddrawer
import numbertoblock
import ledmatrixdrawer
import pygame
import time
import datetime

def run_game():
    color_playground = object_playground.Playground(20, 10)
    red_playground = object_playground.Playground(8, 32)
    led_matrix_drawer = ledmatrixdrawer.LedMatrixDrawer()
    rgb_led_drawer = rgbleddrawer.RgbLedDrawer()
    while True:
        color_playground.clear()
        red_playground.clear()

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

        rgb_led_drawer.draw_playground(color_playground)
        led_matrix_drawer.draw_playground(red_playground)
        pygame.time.Clock().tick(1)

        # rand = random_blocks.Randomblock()
        # next_block = rand.get_random_block()
    color_playground.clear()
    red_playground.clear()