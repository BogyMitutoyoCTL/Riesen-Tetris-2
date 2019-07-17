import controller
import pygame
import tetris_blocks



class Rotater():
    def control(self, g, blo: tetris_blocks.Block):

        returned = g.steuern()
        if returned == "Right!":

            blo.rotation(1)

        if returned == "Left!":

            blo.rotation(-1)