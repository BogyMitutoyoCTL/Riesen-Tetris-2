import time
import tetris_blocks
import pygame
import Colors


class Controller:
    def __init__(self, Joy):
        self.Joy = Joy
    def steuern(self):
        pygame.event.get()
        if self.Joy.get_button(1) > 0.001:
            right = "Right!"
            return right

        if self.Joy.get_button(0) > 0.001:
            e = tetris_blocks.Block(tetris_blocks.Blocktype.t, Colors.Block_color.yellow)
            e.rotation(-1)
            left = "Left!"
            return left

        if self.Joy.get_button(7) > 0.001:
            end = "End!"
            return end

        if self.Joy.get_axis(0) < -0.001:
            go_left = "Go Left!"
            return go_left

        if self.Joy.get_axis(0) > 0.001:
            go_right = "Go Right!"
            return go_right

        if self.Joy.get_axis(1) > 0.001:
            go_down = "Go Down!"
            return go_down