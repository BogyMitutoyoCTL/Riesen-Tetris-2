from color import ObjectColor


def print_object(object):
    size_x = len(object)
    size_y = len(object[0])
    print("")
    for x in range(0, size_x):
        for y in range(0, size_y):
            print(object[x][y], end=" ")
        print("")
    print("")


class Object:
    def __init__(self, field, color):
        self.color = color
        self.orientation = 0
        self.field_with_rotations = field

    def height(self):
        return len(self.get_field())

    def width(self):
        return len(self.get_field()[0])

    def set_color(self, color):
        self.color = color

    def get_field(self):
        return self.field_with_rotations[self.orientation]

    def draw_block(self):
        for x in self.field_with_rotations[self.orientation]:
            print(x)


class Objecttype:
    paddle_left =   [[1, 0, 0],
                     [1, 0, 0],
                     [1, 0, 0]]

    paddle_right = [[0, 0, 1],
                    [0, 0, 1],
                    [0, 0, 1]]

    ball = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]