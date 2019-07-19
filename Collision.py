from playground import Playground
from tetris_blocks import Block


class Collision_Dedektor:

    def collision(self, p: Playground, b: Block, cx, cy):
        for y in range(0, b.height):
            if (y + cy) > p.height:
                break
            for x in range(0, b.width):
                num = b.get_field()[y][x]
                color = p.get_pixel(x + cx, y + cy)
                if self.collision_pixel(color, num):
                    return True

        return False

    def collision_pixel(self, c: tuple, number):
        if number == 0:  # block has no pixel
            return False

        if (c[0] + c[1] + c[2]) == 0:  # field is black
            return False

        return True

    def check_if_block_on_ground(self, p: Playground, b: Block, block_pos_y: int):
        block_hight = len(b.field_with_rotations[0])
        block_width = len(b.field_with_rotations)
        playground_hight = p.height

        for y in range(block_hight):
            for x in range(block_width):
                if b.get_field()[y][x] == 1:
                    if x + block_pos_y > playground_hight - 1:
                        return True
        return False

    def check_if_block_at_wall_right(self, p: Playground, b: Block, block_pos_x: int):
        block_hight = len(b.field_with_rotations[0])
        block_width = len(b.field_with_rotations)
        playground_width = p.width

        for y in range(block_hight):
            for x in range(block_width):
                if b.get_field()[y][x] == 1:
                    if x + block_pos_x > playground_width - 1:
                        return True
        return False

    def check_if_block_at_wall_left(self, p: Playground, b: Block, block_pos_x: int):
        block_hight = len(b.field_with_rotations[0])
        block_width = len(b.field_with_rotations)
        playground_width = p.width

        for y in range(block_hight):
            for x in range(block_width):
                if b.get_field()[y][x] == 1:
                    if x + block_pos_x < 0:
                        return True
        return False

    def inside(self, x, y):
        return 0 <= y < 4 and 0 <= x < 4
