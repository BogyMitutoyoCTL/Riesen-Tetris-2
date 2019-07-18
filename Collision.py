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
                num = b.get_field()[y][x]
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

    def check_if_block_on_ground(self, p:Playground, b:Block, block_pos_y:int):
        block_hight = len(b.field_with_rotations[0])
        block_width = len(b.field_with_rotations)
        playground_hight = p.height

        for y in range(block_hight):
            for x in range(block_width):
                if b.get_field()[y][x] == 1:
                    if y +block_pos_y > playground_hight -1:
                        return True
        return False


    def check_if_block_at_wall(self, p:Playground, b:Block, block_pos_x:int):
        block_hight = len(b.field_with_rotations[0])
        block_width = len(b.field_with_rotations)
        playground_width = p.width

        for y in range(block_hight):
            for x in range(block_width):
                if b.get_field()[y][x] == 1:
                    if y + block_pos_x > playground_width - 2:
                        return True
        return False

    def inside(self, x, y):
        return 0<= y< 4 and 0 <= x < 4