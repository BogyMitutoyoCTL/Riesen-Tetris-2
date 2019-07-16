from Colors import Block_color


class Block:
    def __init__(self, field, Color):
        self.color = Color
        self.field = field

    def set_color(self, color):
        self.color = color

    def draw_block(self):
        for x in self.field:
            print(x)

class Blocktype:
    t = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 1, 0]]

    z_left = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [1, 1, 0, 0],
              [0, 1, 1, 0]]

    z_right = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 1, 1],
               [0, 1, 1, 0]]

    i = [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0]]

    square = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0]]

    l_left = [[0, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [1, 1, 0, 0]]

    l_right = [[0, 0, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 1, 1]]

block_list = [Block(Blocktype.t, Block_color.pink),
              Block(Blocktype.z_left, Block_color.red),
              Block(Blocktype.z_right, Block_color.turquoise),
              Block(Blocktype.i, Block_color.green),
                Block(Blocktype.square, Block_color.yellow),
                Block(Blocktype.l_left, Block_color.darkblue)]