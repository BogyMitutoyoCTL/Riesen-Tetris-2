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

a = Block(Blocktype.t, Block_color.pink)
b = Block(Blocktype.z_left, Block_color.red)
c = Block(Blocktype.z_right, Block_color.turquoise)
d = Block(Blocktype.i, Block_color.green)
e = Block(Blocktype.square, Block_color.yellow)
f = Block(Blocktype.l_left, Block_color.darkblue)
g = Block(Blocktype.l_right, Block_color.orange)


