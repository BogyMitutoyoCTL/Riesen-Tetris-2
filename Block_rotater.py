import controller
import pygame
import tetris_blocks


class Rotater():
    def control(self, g, blo: tetris_blocks.Block):

        returned = g.steuern()
        if returned == "Right!":
            blo.rotate(True)

        if returned == "Left!":
            blo.rotate(False)
