class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def get_color(self):
        return self.red, self.green, self.blue


class BlockColor:
    darkblue = Color(0, 0, 139)

    yellow = Color(255, 255, 0)

    green = Color(0, 128, 0)

    red = Color(255, 0, 0)

    pink = Color(255, 20, 174)

    orange = Color(255, 140, 0)

    turquoise = Color(135, 206, 250)
class ObjectColor:
    yellow =Color(255, 255, 0)

    red =   Color(255, 0, 0)