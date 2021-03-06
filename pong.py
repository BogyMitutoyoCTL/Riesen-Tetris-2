import objects
import ledmatrixdrawer
import object_playground
import points
# import random_blocks
import rgbleddrawer
import controller
import pygame
import numbertoblock
import datetime
import Pong_collisions
import gamespeed
import time
import random
import Ball_Steuerung


def titlescreen(rgb:rgbleddrawer.RgbLedDrawer(), playground:object_playground.Playground, ball, paddle_top, paddle_bot):
    paddle_top.posx = 4
    paddle_bot.posx = 4
    paddle_top.posy = 0
    paddle_bot.posy = 19
    ball.posx = 5

    playground.add_object(paddle_top, paddle_top.posx, paddle_top.posy)
    playground.add_object(paddle_bot, paddle_bot.posx, paddle_bot.posy)
    ball.posy = 7
    playground.add_object(ball, ball.posx, ball.posy)

def run_game():
    # variables for objects
    paddle_left = objects.object_list[0]
    paddle_right = objects.object_list[1]
    paddle_top = objects.object_list[2]
    paddle_bot = objects.object_list[3]
    ball = objects.object_list[4]

    anfang = random.random()
    # Some stuff needed by PyGame
    pygame.init()
    gameover_sound = pygame.mixer.Sound('./Music/GameOver.wav')
    abpraller_sound = pygame.mixer.Sound('./Music/break.wav')
    fail = pygame.mixer.Sound('./Music/fail_sound.wav')

    # use Joystick and Controller
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    joystick2 = pygame.joystick.Joystick(1)
    joystick2.init()

    gamepad = controller.Controller(joystick)
    gamepad2 = controller.Controller(joystick2)

    # drawer for playfield
    rgb_led_drawer = rgbleddrawer.RgbLedDrawer()

    # drawer for scoreboard
    led_matrix_drawer = ledmatrixdrawer.LedMatrixDrawer()

    # Playgrounds
    color_playground = object_playground.Playground(20, 10)
    red_playground = object_playground.Playground(8, 32)
    color_playground.clear()

    titlescreen(rgb_led_drawer, color_playground, ball, paddle_top, paddle_bot)
    # Prepare red_playgound to repaint...
    # red_playground.clear()
    # color_playground.clear()
    # Add preview block to red_playgound
    i = 0
    paddle_top.posx = 4
    paddle_bot.posx = 4
    paddle_top.posy = 0
    paddle_bot.posy = 19
    ball.posx = 5

    color_playground.add_object(paddle_top, paddle_top.posx, paddle_top.posy)
    color_playground.add_object(paddle_bot, paddle_bot.posx, paddle_bot.posy)
    if anfang > 0.5:
        ball.posy = 7
        color_playground.add_object(ball, ball.posx, ball.posy)
        ball.orientation_y = 1
    else:
        ball.posy = 12
        color_playground.add_object(ball, ball.posx, ball.posy)
        ball.orientation_y = -1
    # draw red_playgound
    rgb_led_drawer.draw_playground(color_playground)
    led_matrix_drawer.draw_playground(red_playground)
    color_playground.clear()
    red_playground.clear()
    score1 = 0
    score2 = 0

    # gamestruktur
    game_over = False
    while game_over == False:
        Runde = 0
        Ball_Steuerung.Ball_Steuerung.ball_orientation(Ball_Steuerung.Ball_Steuerung, ball)
        time_to_wait = 500 - 50 * (score1 + score2)
        ball.posx = 5
        while True:
            Runde += 1
            gamepad.Paddle_Steuerung(paddle_top)
            while paddle_top.posx > 7:
                paddle_top.posx -= 1
            while paddle_top.posx < 0:
                paddle_top.posx += 1
            # bot_steuerung_mit_fail(paddle_top,ball)
            #gamepad2.Paddle_Steuerung(paddle_bot)
            #while paddle_bot.posx > 7:
                #paddle_bot.posx -= 1
            #while paddle_bot.posx < 0:
                #paddle_bot.posx += 1
            bot_steuerung_mit_fail(paddle_bot, ball, score1)
            color_playground.add_object(paddle_top, paddle_top.posx, paddle_top.posy)
            color_playground.add_object(paddle_bot, paddle_bot.posx, paddle_bot.posy)
            red_playground.add_block(numbertoblock.NumberToBlock.get_block_einzelne_zahl(score1), 0, 0)
            red_playground.add_block(numbertoblock.NumberToBlock.get_block_einzelne_zahl(score2), 24, 0)
            if ball.posx == 0:
                Runde += 1
                ball.orientation_x = -ball.orientation_x
                pygame.mixer.Sound.play(abpraller_sound)

            if ball.posx == 9:
                Runde += 1
                ball.orientation_x = -ball.orientation_x
                pygame.mixer.Sound.play(abpraller_sound)

            if Pong_collisions.Collision_Dedektor.with_object(Pong_collisions.Collision_Dedektor, color_playground, ball, ball.posx + ball.orientation_x, ball.posy + ball.orientation_y) == True:
                Runde += 1
                ball.orientation_y = -ball.orientation_y
                pygame.mixer.Sound.play(abpraller_sound)
                if time_to_wait > 0:
                    time_to_wait -= 10
            if object_is_above_beginning(ball) == True:
                score2 += 1
                ball.posy = 12
                red_playground.clear()
                red_playground.add_block(numbertoblock.NumberToBlock.get_block_einzelne_zahl(score1), 0, 0)
                red_playground.add_block(numbertoblock.NumberToBlock.get_block_einzelne_zahl(score2), 24, 0)
                led_matrix_drawer.draw_playground(red_playground)
                break
            if object_is_below_bottom(ball) == True:
                score1 += 1
                ball.posy = 7
                red_playground.clear()
                red_playground.add_block(numbertoblock.NumberToBlock.get_block_einzelne_zahl(score1), 0, 0)
                red_playground.add_block(numbertoblock.NumberToBlock.get_block_einzelne_zahl(score2), 24, 0)
                led_matrix_drawer.draw_playground(red_playground)
                pygame.mixer.Sound.play(fail)
                break

            ball.posx = ball.posx + ball.orientation_x
            ball.posy = ball.posy + ball.orientation_y

            color_playground.add_object(ball, ball.posx, ball.posy)
            rgb_led_drawer.draw_playground(color_playground)
            led_matrix_drawer.draw_playground(red_playground)
            color_playground.clear()
            red_playground.clear()

            pygame.time.wait(time_to_wait - Runde)
        if score1 == 3:
            pygame.time.wait(3000)
            game_over = True
            break
        if score2 == 3:
            pygame.time.wait(3000)
            game_over = True
            break
        pygame.time.wait(3000)

        color_playground.clear()
        red_playground.clear()

    pygame.mixer.Sound.play(gameover_sound)
    # Spiel
    pygame.time.wait(5000)
    del led_matrix_drawer
    del rgb_led_drawer
    pygame.event.get()


def object_is_above_beginning(object):
    if object.posy <= 0:
        return True
    return False


def object_is_below_bottom(object):
    if object.posy >= 19:
        return True
    return False


def check_for_full_lines(calculator, color_playground, full_line_detector, score):
    lines = full_line_detector.detect_lines(color_playground)
    full_line_detector.delete_full_lines(lines, color_playground)
    score = calculator.points(score, len(lines), 0)
    return score


def round(b: object, b1: object, b2: object, c: Pong_collisions.Collision_Dedektor, p: object_playground, bs: Ball_Steuerung, joy1,
          joy2):
    Ball_Steuerung.position_calculator(bs, p, b1, b2, c, b)
    # Controller.Paddle_Steuerung(joy1, b1)
    # Controller.Paddle_Steuerung(joy2, b2)


def bot_steuerung_mit_fail(s:object,b:object,score1):
    scorediff = 0
    if score1 == 1:
        scorediff = 0.5
    if score1 == 2:
        scorediff = 1
    fail = random.random()
    if fail > 0.3-scorediff:
        if s.posx-b.posx >= 0:
            if s.posx > 0:
                s.posx -= 1
        if s.posx-b.posx+2 <= 0:
            if s.posx < 7:
                s.posx += 1

def bot_steuerung(s:object,b:object):
    if s.posx-b.posx >= 0:
        if s.posx > 0:
            s.posx -= 1
    if s.posx-b.posx+2 <= 0:
        if s.posx < 7:
            s.posx += 1


if __name__ == "__main__":
    while True:
        run_game()
