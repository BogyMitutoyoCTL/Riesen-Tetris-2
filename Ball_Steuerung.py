import Collision
import playground
from objects import Object
from random import random

class Ball_Steuerung:

    def orientation_scanner(self, p:playground, b1:Object, b2:Object, c:Collision.Collision_Dedektor, b:Object):
        if(Collision.Collision_Dedektor.at_wall(c, p, b,b.posy) == True):
            b.orientation_y = -b.orientation_y
        if (Collision.Collision_Dedektor.with_object(p, b1, b.posx, b.posy) == True):
            b.orientation_x = -b.orientation_x
        if (Collision.Collision_Dedektor.with_object(p, b2, b.posx, b.posy) == True):
            b.orientation_x = -b.orientation_x

    def position_calculator(self, p:playground, b1: Object, b2:Object, c:Collision.Collision_Dedektor,b:Object):
        self.orientation_scanner(p, b1, b2, c, b)
        b.posx = b.posx + b.orientation_x
        b.posy = b.posy + b.orientation_y

    def ball_orientation(self, b:object):
        randomint = random.randint(1, 2)
        if randomint == 1 :
            b.orientation_x = -1
        if randomint == 2 :
            b.orientation_x = 1

        randomint = random.randint(1, 2)
        if randomint == 1 :
            b.orientation_y = -1
        if randomint == 2 :
            b.orientation_y = 1

    def end_game(self, p:playground, b:object, c:Collision.Collision_Dedektor):
        if( (c.on_ground(p, b, b.posy) == True ) or ( c.on_top( (p, b, b.posy) == True) ) ):
            return True