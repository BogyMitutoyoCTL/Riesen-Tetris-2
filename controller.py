import pygame
from objects import Object
from pygame.joystick import Joystick
import Pong_collisions
import object_playground

class Controller:
    def __init__(self, joystick: Joystick):
        self.Joy = joystick

    def get_button_pressed(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
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
                if hat_x == 1 and hat_y == 0:
                    paddle.posx += 1 #right
                if hat_x == -1 and hat_y == 0:
                    paddle.posx -=1 #left
            if event.type == pygame.JOYAXISMOTION:
                x = self.Joy.get_axis(0)
                if x > 0.3:
                    paddle.posx += 1
                if x < -0.3:
                    paddle.posx -= 1

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 4:
                    paddle.posx -=1
                if event.button == 5:
                    paddle.posx +=1