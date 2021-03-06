import Pong_collisions
import object_playground
import pong
from objects import Object
import random

class Ball_Steuerung:

    def orientation_scanner(self, p:object_playground, paddle1:Object, paddle2:Object, c:Pong_collisions.Collision_Dedektor, ball:Object):
        if (Pong_collisions.Collision_Dedektor.with_object(c, p, ball, ball.posx, ball.posy) == True):
            ball.orientation_y = -ball.orientation_y

    def position_calculator(self, p:object_playground, b1: Object, b2:Object, c:Pong_collisions.Collision_Dedektor, b:Object):
        self.orientation_scanner(Ball_Steuerung, p, b1, b2, c, b)
        b.posx = b.posx + b.orientation_x
        b.posy = b.posy + b.orientation_y

    def ball_orientation(self, b:object):
        randomint = random.randint(1,2)
        if randomint == 1:
            b.orientation_x = -1
        if randomint == 2:
            b.orientation_x = 1
