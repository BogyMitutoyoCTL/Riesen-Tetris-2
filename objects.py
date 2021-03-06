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
        self.field = field
        self.orientation_x = 0
        self.orientation_y = 0
        self.posx = 0
        self.posy = 0

    @property
    def height(self):
        return len(self.field)

    @property
    def width(self):
        return len(self.field[0])

    def set_color(self, color):
        self.color = color

    def get_field(self):
        return self.field

    def draw_object(self):
        for x in self.field:
            print(x)


class Objecttype:
    paddle_left =   [[1, 0, 0],
                     [1, 0, 0],
                     [1, 0, 0]]

    paddle_right = [[0, 0, 1],
                    [0, 0, 1],
                    [0, 0, 1]]

    paddle_top =   [[1, 1, 1]]

    paddle_bot =   [[1, 1, 1]]

    ball =      [[1]]

object_list = [Object(Objecttype.paddle_left, ObjectColor.yellow),
               Object(Objecttype.paddle_right, ObjectColor.yellow),
               Object(Objecttype.paddle_top, ObjectColor.yellow),
               Object(Objecttype.paddle_bot, ObjectColor.yellow),
               Object(Objecttype.ball, ObjectColor.red)]
