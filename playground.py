class Playground:
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
        self.list_pixel = [(100,0,0)] * (hight * width)

    def add_block(self):
        pass

    def draw(self):
        for x in range(self.hight):
            for y in range(self.width):
                print(self.list_pixel[x * y], end=' ')
            print("")

    def get_pixel(self, x, y):
        return self.list_pixel[x * y]


p = Playground(20, 10)

p.add_block()

p.draw()
