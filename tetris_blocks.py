from Colors import Block_color


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
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        line_nr = 0
        column_nr = 0
        for line in self.field_with_rotations[self.orientation]:
            for pos in line:
                print("Pos(" + str(line_nr) + "/" + str(column_nr) + ") " + str(pos), end=" ")
                #
                # Hier in die 8x8 Matrix schreiben
                #
                column_nr += 1
            # Für Zeilenschaltung
            print("")
            line_nr += 1
            column_nr = 0


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
