import tetris_blocks


class Playground:
    def __init__(self, hight, width):
        self.height = hight
        self.width = width
        self.list_pixel = []
        self.clear()

    def clear(self):
        self.list_pixel = []
        for h in range(self.height):
            for i in range(self.width):
                self.list_pixel.append((0, 0, 0))

    def add_block(self, block: tetris_blocks.Block, columns_right, lines_down):
        x_of_block = 0
        y_of_block = 0
        for h in block.get_field():
            for ispixel in h:
                pixelnumber = x_of_block * self.width + y_of_block + lines_down * self.width + columns_right

                if pixelnumber > self.height * self.width - 1:
                    return

                if ispixel > 0:
                    self.list_pixel[pixelnumber] = block.color.get_color()

                y_of_block += 1

            y_of_block = 0
            x_of_block += 1

    def block_clear(self, block: tetris_blocks.Block, columns_right, lines_down):
        x_of_block = 0
        y_of_block = 0
        for h in block.get_field():
            for ispixel in h:
                pixelnumber = x_of_block * self.width + y_of_block + lines_down * self.width + columns_right

                if pixelnumber > self.height * self.width - 1:
                    return

                if ispixel > 0:
                    self.list_pixel[pixelnumber] = (0, 0, 0)

                y_of_block += 1

            y_of_block = 0
            x_of_block += 1

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                print(self.list_pixel[y * self.width + x], end=' ')
            print("")

    def get_pixel(self, x, y):
        return self.list_pixel[y * self.width + x]
