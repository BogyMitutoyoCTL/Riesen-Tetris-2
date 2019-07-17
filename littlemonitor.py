from luma.core.render import canvas


class draw_small:
    def __init__(self, device):
        self.device = device

    def draw_playground(self, playground):
        with canvas(self.device)as draw:
            for x in range(0, playground.width):
                for y in range(0, playground.hight):
                    color = playground.get_pixel(x, y)
                    if color[0] >= 1 or color[1] >= 1 or color[2] >= 1:
                        draw.point((x, y), fill="white")
                    else:
                        draw.point((x, y), fill="black")
