import Colors
from playground import Playground
from tetris_blocks import Block


class Collision_Dedektor:

    def collision(self, p:Playground, b:Block, cx, cy):

        collision = 0
        for y in range(0, 4):

            if (y + cy)>19:
                break

            for x in range(0, 4):
                num = b.get_field()[x][y]
                color = p.get_pixel(x + cx, y + cy)
                collision += self.collision_pixel(color, num)

        if collision > 0:
            return True
        else:
            return False



    def collision_pixel(self, c:tuple, number):
        if (c[0] + c[1] + c[2]) == 0:
            color = 0

        else:
            color = 1

        col = color * number
        return col

