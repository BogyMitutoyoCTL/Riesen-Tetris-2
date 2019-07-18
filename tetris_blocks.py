from color import BlockColor


def print_block(block):
    size_x = len(block)
    size_y = len(block[0])
    print("")
    for x in range(0, size_x):
        for y in range(0, size_y):
            print(block[x][y], end=" ")
        print("")
    print("")


class Block:
    def __init__(self, field, Color):
        self.color = Color
        self.field_with_rotations = field
        self.orientation = 0

    def set_color(self, color):
        self.color = color

    def get_field(self):
        return self.field_with_rotations[self.orientation]

    def draw_block(self):
        for x in self.field_with_rotations[self.orientation]:
            print(x)

    def rotation(self, orientation: int):
        if 0 <= orientation <= len(self.field_with_rotations):
            self.orientation = orientation

    def rotate(self, left: bool = True):
        orientation = self.orientation
        if left:
            orientation += 1
        else:
            orientation += -1
        orientation_value = orientation % len(self.field_with_rotations)
        self.orientation = orientation_value

    def rotate_old(self, direction: int):

        self.orientation += direction
        if self.orientation == 4:
            self.orientation = 0
        if self.orientation == -1:
            self.orientation = 3

    def strech_block_twice(self):
        block_array = []
        for i in range(len(self.field_with_rotations)):
            matrix_8_8 = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0]]

            size_x = len(self.field_with_rotations[i])
            size_y = len(self.field_with_rotations[i][0])
            for x in range(0, size_x):
                for y in range(0, size_y):
                    if self.field_with_rotations[i][x][y] > 0:
                        matrix_8_8[x * 2][y * 2] = 1
                        matrix_8_8[x * 2 + 1][y * 2] = 1
                        matrix_8_8[x * 2][y * 2 + 1] = 1
                        matrix_8_8[x * 2 + 1][y * 2 + 1] = 1

            block_array.append(matrix_8_8)
        return Block(block_array, self.color)


# verdoppelt Blöcke
# def turn_block(self):


class Blocktype:
    t = [[[0, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],

         [[1, 0, 0, 0],
          [1, 1, 0, 0],
          [1, 0, 0, 0],
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

              [[0, 0, 0, 1],
               [0, 0, 1, 1],
               [0, 0, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 1, 1],
               [0, 1, 1, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 1],
               [0, 0, 1, 1],
               [0, 0, 1, 0],
               [0, 0, 0, 0]]]

    z_right = [[[0, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]],

               [[1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]],

               [[1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]]

    i = [[[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]],

         [[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],

         [[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]],

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

    l_left = [[[0, 0, 0, 1],
               [0, 0, 0, 1],
               [0, 0, 1, 1],
               [0, 0, 0, 0]],

              [[0, 1, 0, 0],
               [0, 1, 1, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],

              [[0, 0, 1, 1],
               [0, 0, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],
               [0, 1, 1, 1],
               [0, 0, 0, 1],
               [0, 0, 0, 0]]]

    l_right = [[[0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 0]],

               [[0, 0, 0, 0],
                [0, 1, 1, 1],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]],

               [[0, 0, 0, 1],
                [0, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]]


block_list = [Block(Blocktype.t, BlockColor.pink),
              Block(Blocktype.z_left, BlockColor.red),
              Block(Blocktype.z_right, BlockColor.turquoise),
              Block(Blocktype.i, BlockColor.green),
              Block(Blocktype.square, BlockColor.yellow),
              Block(Blocktype.l_left, BlockColor.darkblue),
              Block(Blocktype.l_right, BlockColor.orange)]

if __name__ == "__main__":
    my_block = Block(Blocktype.t, BlockColor.pink)
    my_block.strech_block_twice()

    for i in range(1000):
        my_block.rotate(True)
