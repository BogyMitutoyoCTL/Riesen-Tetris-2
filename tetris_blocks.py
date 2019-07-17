from Colors import Block_color

def print_block(block):
    size_x = len(block)
    size_y = len(block[0])
    for x in range(0, size_x):
        for y in range(0, size_y):
            print(block[x][y], end=" ")
        print("")


class Block:
    def __init__(self, field, Color):
        self.color = Color
        self.field_with_rotations = field
        self.orientation = 0

    def set_color(self, color):
        self.color = color

    def draw_block(self):
        for x in self.field_with_rotations[self.orientation]:
            print(x)

    def rotation(self, orientation: int):
        if 0 <= orientation <= len(self.field_with_rotations):
            self.orientation = orientation

    def strech_block_twice(self):
        matrix_8_8 = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        size_x = 0
        size_y = 0
        size_x = len(self.field_with_rotations[self.orientation])
        size_y = len(self.field_with_rotations[self.orientation][0])
        for x in range(0, size_x):
            for y in range(0, size_y):
                if self.field_with_rotations[self.orientation][x][y] > 0:
                    matrix_8_8[x*2][y*2] = 1
                    matrix_8_8[x*2+1][y*2] = 1
                    matrix_8_8[x*2][y*2+1] = 1
                    matrix_8_8[x*2+1][y*2+1] = 1

        print_block(matrix_8_8)
        return matrix_8_8
#verdoppelt Blöcke
# def turn_block(self):


class Blocktype:
    t = [[[0, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],

         [[0, 1, 0, 0],
          [0, 1, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]],

         [[0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]],

         [[0, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]]]

    z_left = [[[0, 1, 1, 0],
               [0, 0, 1, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],

              [[0, 1, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0]],

              [[0, 1, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0]]]

    z_right = [[[0, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]],

               [[0, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 0, 0, 0],
                [0, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]]

    i = [[[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]],

         [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0]],

         [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]],

         [[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]]

    square = [[[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]]]

    l_left = [[[0, 0, 1, 0],
               [0, 0, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],
               [1, 1, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0]],

              [[0, 1, 1, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]],

              [[1, 0, 0, 0],
               [1, 1, 1, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]]

    l_right = [[[0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]],

               [[0, 0, 0, 0],
                [0, 1, 1, 1],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]],

               [[0, 0, 1, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]]


block_list = [Block(Blocktype.t, Block_color.pink),
              Block(Blocktype.z_left, Block_color.red),
              Block(Blocktype.z_right, Block_color.turquoise),
              Block(Blocktype.i, Block_color.green),
              Block(Blocktype.square, Block_color.yellow),
              Block(Blocktype.l_left, Block_color.darkblue),
              Block(Blocktype.l_right, Block_color.orange)]

# block_list[0].draw_block()

block_list[0].strech_block_twice()
