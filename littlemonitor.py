import tetris_blocks
import time
import argparse
import playground
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

p2 = playground.Playground(8, 32)


class draw_small:
    def __init__(self, device):
        self.device = device

    def draw_playground(self, playground):
        with canvas(device)as draw:
            for x in range(0, playground.width):
                for y in range(0, playground.hight):
                    color = playground.get_pixel(x, y)
                    if color[0] >= 1 or color[1] >= 1 or color[2] >= 1:
                        draw.point((x, y), fill="White")


p2.draw()

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90,
                 rotate=0, blocks_arranged_in_reverse_order=True)
Max = draw_small(device)
p2.add_block(tetris_blocks.block_list[3])
Max.draw_playground(p2)
time.sleep(20)
