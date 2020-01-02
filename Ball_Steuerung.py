import Collision
import playground
import pong
from objects import Object
import random

class Ball_Steuerung:

    def orientation_scanner(self, p:playground, b1:Object, b2:Object, c:Collision.Collision_Dedektor, b:Object):
        if (Collision.Collision_Dedektor.with_object(c, p, b, b.posx, b.posy) == True):
            b.orientation_y = -b.orientation_y
        if (Collision.Collision_Dedektor.with_object(c, p, b, b.posx, b.posy) == True):
            b.orientation_y = -b.orientation_y

    def position_calculator(self, p:playground, b1: Object, b2:Object, c:Collision.Collision_Dedektor,b:Object):
        self.orientation_scanner(Ball_Steuerung, p, b1, b2, c, b)
        b.posx = b.posx + b.orientation_x
        b.posy = b.posy + b.orientation_y

    def ball_orientation(self, b:object):
        randomint = random.randint(1,2)
        if randomint == 1:
            b.orientation_x = -1
        if randomint == 2:
            b.orientation_x = 1

        randomint = random.randint(1, 2)
        if randomint == 1 :
            b.orientation_y = -1
        if randomint == 2 :
            b.orientation_y = 1

    def end_game(self, b:object):
        if b.posy == 0 or b.posy == 19:
            return True