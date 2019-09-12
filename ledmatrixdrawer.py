from luma.core.render import canvas
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from playground import Playground


class LedMatrixDrawer:
    def __init__(self):
        serial = spi(port=0, device=0, gpio=noop())
        led_matrix = max7219(serial, cascaded=4, block_orientation=90,
                             rotate=0, blocks_arranged_in_reverse_order=True)
        self.device = led_matrix

    def draw_playground(self, playground: Playground):
        with canvas(self.device)as draw:
            for x in range(0, playground.width):
                for y in range(0, playground.height):
                    color = playground.get_pixel(x, y)
                    if color[0] >= 1 or color[1] >= 1 or color[2] >= 1:
                        draw.point((x, y), fill="white")
                    else:
                        draw.point((x, y), fill="black")
