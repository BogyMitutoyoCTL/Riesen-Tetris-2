from playground import Playground
from objects import Object

class Collision_Dedektor:

    def with_object(self, p: Playground, b: Object, cx, cy):
        for y in range(0, b.height):
            for x in range(0, b.width):
                num = b.get_field()[y][x]
                if p.is_inside_field(x + cx, y + cy):
                    color = p.get_pixel(x + cx, y + cy)
                    if self.is_collision(self, color, num):
                        return True

        return False

    def is_collision(self, c: tuple, number):
        if number == 0:  # block has no pixel
            return False

        if (c[0] + c[1] + c[2]) == 0:  # field is black
            return False

        return True

    def on_ground(self, p: Playground, b: Object, block_pos_y: int):
        for y in range(b.height):
            for x in range(b.width):
                if b.get_field()[y][x] == 1:
                    if not p.is_inside_field(x, y + block_pos_y+1):
                        return True
        return False

    def on_top(self, p: Playground, b: Object, block_pos_y: int):
        if b.posy + b.height > p.height - 1 :
            return True

    def at_wall(self, p: Playground, b: Object, block_pos_x: int):
        playground_width = p.width

        for y in range(b.height):
            for x in range(b.width):
                if b.get_field()[y][x] == 1:
                    if x + block_pos_x > playground_width - 1:  # hits right wall
                        return True
                    if x + block_pos_x < 0:  # hits left wall
                        return True
        return False
