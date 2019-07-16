class Playground:
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
        self.list_pixel = []
        for h in range(hight):
            for i in range(width):
                self.list_pixel.append((i*10,0,h*10))

    def add_block(self):
        pass

    def draw(self):
        for x in range(self.hight):
            for y in range(self.width):
                print(self.list_pixel[y*10+x], end=' ')
            print("")

    def get_pixel(self, x, y):
        return self.list_pixel[y*10+x]


p = Playground(20, 10)

p.add_block()

p.draw()
