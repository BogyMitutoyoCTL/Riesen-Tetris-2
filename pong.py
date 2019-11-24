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
import objects


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

        result = controller.get_button_pressed((1, 1), Collision.Collision_Dedektor(),
                                               Playground.Playground(20, 10))
        if result == "Restart":
            break
    color_playground.clear()
    red_playground.clear()


def run_game():
    # Some stuff needed by PyGame
    pygame.init()

    # use Joystick and Controller
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # todo: new sounds
    pygame.mixer.init()
    pygame.mixer.music.load('./Music/Tetris Edit 1 Export 3.mp3')
    new_block = pygame.mixer.Sound('./Music/New_Block.wav')
    game_over_sound = pygame.mixer.Sound('./Music/GameOver.wav')
    break_sound = pygame.mixer.Sound('./Music/break.wav')
    lines1_3 = pygame.mixer.Sound('./Music/1.-3.lane.wav')
    line4 = pygame.mixer.Sound('./Music/4.lane.wav')
    # pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    gamepad = Controller.Controller(joystick)

    # drawer for playfield
    rgg_led_drawer = rgbleddrawer.RgbLedDrawer()

    # drawer for scoreboard
    led_matrix_drawer = Matrix_Drawer.LedMatrixDrawer()

    # Playgrounds
    color_playground = Playground.Playground(20, 10)
    red_playground = Playground.Playground(8, 32)

    score1 = 0
    score2 = 0
    collision = Collision.Collision_Dedektor()

    clock = pygame.time.Clock()  # type: pygame.time.Clock
    clock_titlescreen(color_playground, rgg_led_drawer, red_playground, led_matrix_drawer, Controller)
    game_over = False
    while not game_over:
        color_playground.add_object(Objects.Objecttype.paddle_left, 3, 3)
        rgg_led_drawer.draw_playground(color_playground)
    #todo: here is were the game is written
    del led_matrix_drawer
    del rgg_led_drawer
    pygame.event.get()
    pygame.quit()


if __name__ == "__main__":
    while True:
        run_game()
