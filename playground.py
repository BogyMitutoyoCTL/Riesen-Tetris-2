import time
import tetris_blocks


class Playground:
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
        self.list_pixel = []
        for h in range(hight):
            for i in range(width):
                self.list_pixel.append((0, 0, 0))

    def add_block(self, block: tetris_blocks.Block):
        pos_x = 0
        pos_y = 0
        for h in block.field:
            for w in h:
                # print(w)
                print("Posx: " + str(pos_x))
                print("Posy: " + str(pos_y))
                if w > 0:
                    self.list_pixel[pos_x * self.width + pos_y] = (100,0,0)
                pos_y += 1
            pos_y = 0
            pos_x += 1

    def draw(self):
        for x in range(self.hight):
            for y in range(self.width):
                print(self.list_pixel[y * self.width + x], end=' ')
            print("")

    def get_pixel(self, x, y):
        return self.list_pixel[y * self.width + x]


p = Playground(20, 10)

p.add_block(tetris_blocks.block_list[0])

p.draw()

