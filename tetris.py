import time
import pygame

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


def run_game():
    # Some stuff needed by PyGame
    pygame.init()

    # use Joystick and Controller
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    pygame.mixer.init()
    pygame.mixer.music.load('./Music/Tetris Edit 1 Export 3.mp3')
    new_block = pygame.mixer.Sound('./Music/New_Block.wav')
    game_over_sound = pygame.mixer.Sound('./Music/GameOver.wav')
    # break_sound = pygame.mixer.Sound('./Music/break.wav')
    lines1_3 = pygame.mixer.Sound('./Music/1.-3.lane.wav')
    # line4 = pygame.mixer.Sound('./Music/4.lane.mp3')
    #pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

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

    score = -1
    collision = Collision.Collision_Dedektor()
    current_block_position = (5, 0)

    full_line_detector = deleteline.FullLineDetector()
    calculator = points.Points()

    clock = pygame.time.Clock()  # type: pygame.time.Clock

    game_over = False
    while not game_over:
        pygame.mixer.Sound.play(new_block)
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
        countdown = 200
        while countdown > 0:
            clock.tick(gamespeed.GameSpeed.game_speed(score))
            countdown = countdown - 1

            color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
            rgg_led_drawer.draw_playground(color_playground)

            if collision.on_ground(color_playground, current_block, current_block_position[1]):
                score = check_for_full_lines(calculator, color_playground, full_line_detector, score)
                break

            color_playground.block_clear(current_block, current_block_position[0], current_block_position[1])

            current_block_position = gamepad.get_button_pressed(current_block, current_block_position, collision,
                                                                color_playground)
            if current_block_position == "Restart":
                game_over = True
                break

            if collision.with_block(color_playground, current_block, current_block_position[0],
                                    current_block_position[1] + 1):
                if block_is_above_beginning(current_block, current_block_position[1]):
                    game_over = True
                    pygame.mixer.Sound.play(game_over_sound)
                    break
                color_playground.add_block(current_block, current_block_position[0], current_block_position[1])
                rgg_led_drawer.draw_playground(color_playground)
                old_score = score
                score = check_for_full_lines(calculator, color_playground, full_line_detector, score)
                new_score = score
                score_diff = new_score - old_score
                if score_diff == 10:
                    red_playground.add_block(numbertoblock.NumberToBlock.get_block(10), 0, 0)
                    led_matrix_drawer.draw_playground(red_playground)
                    pygame.mixer.Sound.play(lines1_3)
                break
            if (countdown%10 == 0):
                current_block_position = (current_block_position[0], current_block_position[1] + 1)

        current_block_position = (color_playground.width // 2, 0)

    del led_matrix_drawer
    del rgg_led_drawer
    pygame.event.get()
    pygame.quit()


def block_is_above_beginning(block, line):
    for y in range(block.height):
        for x in range(block.width):
            if block.get_field()[y][x] == 1:
                if y + line <= 0:
                    return True
    return False


def check_for_full_lines(calculator, color_playground, full_line_detector, score):
    lines = full_line_detector.detect_lines(color_playground)
    full_line_detector.delete_full_lines(lines, color_playground)
    score = calculator.points(score, len(lines), 0)
    return score


if __name__ == "__main__":
    while True:
        run_game()

