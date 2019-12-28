import Collision
import playground
from objects import Object


class Ball_Steuerung:

    def orientation_scanner(self, p:playground, b1:Object, b2:Object, c:Collision.Collision_Dedektor, b:Object):
        if(Collision.Collision_Dedektor.on_top(c, p, b,b.posy) == True):
            b.orientation_y = -b.orientation_y
        if (Collision.Collision_Dedektor.on_ground(c, p, b, b.posy) == True):
            b.orientation_y = -b.orientation_y
        if (Collision.Collision_Dedektor.with_object(p, b1, b.posx, b.posy) == True):
            b.orientation_x = -b.orientation_x
        if (Collision.Collision_Dedektor.with_object(p, b2, b.posx, b.posy) == True):
            b.orientation_x = -b.orientation_x

    def position_calculator(self, p:playground, b1: Object, b2:Object, c:Collision.Collision_Dedektor,b:Object):
        self.orientation_scanner(p, b1, b2, c, b)
        b.posx = b.posx + b.orientation_x
        b.posy = b.posy + b.orientation_y