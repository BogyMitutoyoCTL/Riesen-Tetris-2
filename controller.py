import pygame
from objects import Object
from pygame.joystick import Joystick
import Collision
from playground import Playground

class Controller:
    def __init__(self, joystick: Joystick):
        self.Joy = joystick

    def get_button_pressed(self):
        events = pygame.event.get()

        for event in events:
            direction = None
            if event.type == pygame.JOYHATMOTION:
                hat_x, hat_y = event.value
                if hat_x == -1 and hat_y == 0:
                    direction = True  # left
                if hat_x == 1 and hat_y == 0:
                    direction = False  # right
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    direction = False  # right
                if event.button == 0:
                    direction = True  # left
                if event.button == 7:
                    return "Restart"
                if event.button == 4:
                    return "Left Title"
                if event.button == 5:
                    return "Right Title"
    def Paddle_Steuerung(self, paddle:Object):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.JOYHATMOTION:
                hat_x, hat_y = event.value
                if hat_x == -1 and hat_y == 1:
                    paddle.orientation_y = -1 #up
                if hat_x == 1 and hat_y == -1:
                    paddle.orientation_y == 1 #down