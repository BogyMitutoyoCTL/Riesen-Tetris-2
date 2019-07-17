import controller
import pygame
import tetris_blocks



class Rotater():
    def control(self, a, blo: tetris_blocks.Block):

        returned = a.steuern()
        if returned == "Right!":

            blo.rotation(1)

        if returned == "Left!":

            blo.rotation(-1)