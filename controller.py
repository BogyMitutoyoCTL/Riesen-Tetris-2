import pygame
from pygame.joystick import Joystick
import Collision
from playground import Playground


class Controller:
    def __init__(self, joystick: Joystick):
        self.Joy = joystick

    def get_button_pressed(self, blo, position, collision: Collision.Collision_Dedektor, playground: Playground):
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
            self.rotate_if_possible(blo, collision, direction, playground, position)

        newposition = None
        if self.Joy.get_axis(0) < -0.3:
            newposition = (position[0] - 1, position[1])

        if self.Joy.get_axis(0) > 0.3:
            newposition = (position[0] + 1, position[1])
        if newposition is not None:
            if not collision.at_wall(playground, blo, newposition[0]) and \
                    not collision.on_ground(playground, blo, newposition[1]) and \
                    not collision.with_block(playground, blo, newposition[0], newposition[1]):
                position = newposition

    def rotate_if_possible(self, blo, collision, direction, playground, position):
        rotate_sound = pygame.mixer.Sound('./Music/rotate.wav')

        if direction is not None:
            blo.rotate(direction)
            if collision.at_wall(playground, blo, position[0]) or \
                    collision.on_ground(playground, blo, position[1]) or \
                    collision.with_block(playground, blo, position[0], position[1]):
                blo.rotate(not direction)
            else:
                pygame.mixer.Sound.play(rotate_sound)