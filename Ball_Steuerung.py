import Collision
import playground
from objects import Object


class Ball_Steuerung:
    def __init__(self):
        orientation = None

    def bounce(self, b1:Object,b2:Object,p:playground, cx, cy):
        if(Collision.Collision_Dedektor.with_object(p, b1, cx, cy)==True):
            newposition = (cx+1, cy)
        if (Collision.Collision_Dedektor.with_object(p, b2, cx, cy) == True):
            newposition = (cx-1, cy)
        if(Collision.Collision_Dedektor.on_ground(p, cy)):
            newposition = (cx, cy+1)
        if(Collision.Collision_Dedektor.on_top(p, cy)):
            newposition = (cx, cy-1)

        return newposition

    def ingame(self, p:playground, b1:Object, b2:Object, position):
        position = self.bounce(b1, b2, p, position[0], position[1])

        return position