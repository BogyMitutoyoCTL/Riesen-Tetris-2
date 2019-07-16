import tetris_blocks
import playground
import time

from luma.core.legacy import text
from luma.core.legacy.font import proportional, TINY_FONT
from luma.core.render import canvas
from luma.led_matrix.device import neopixel

from Colors import Block_color


class draw:
    def __init__(self, device, ):
        self.device = device

    def draw_playground(self, playground):
        with canvas(device)as draw:
            for x in range(0, playground.width):
                for y in range(0, playground.hight):
                    color = playground.get_pixel(x, y)
                    draw.point((x, y), fill=color)


HAT = [
    0, 20, 40, 60, 80, 100, 120, 140, 160, 180,
    1, 21, 41, 61, 81, 101, 121, 141, 161, 181,
    2, 22, 42, 62, 82, 102, 122, 142, 162, 182,
    3, 23, 43, 63, 83, 103, 123, 143, 163, 183,
    4, 24, 44, 64, 84, 104, 124, 144, 164, 184,
    5, 25, 45, 65, 85, 105, 125, 145, 165, 185,
    6, 26, 46, 66, 86, 106, 126, 146, 166, 186,
    7, 27, 47, 67, 87, 107, 127, 147, 167, 187,
    8, 28, 48, 68, 88, 108, 128, 148, 168, 188,
    9, 29, 49, 69, 89, 109, 129, 149, 169, 189,
    10, 30, 50, 70, 90, 110, 130, 150, 170, 190,
    11, 31, 51, 71, 91, 111, 131, 151, 171, 191,
    12, 32, 52, 72, 92, 112, 132, 152, 172, 192,
    13, 33, 53, 73, 93, 113, 133, 153, 173, 193,
    14, 34, 54, 74, 94, 114, 134, 154, 174, 194,
    15, 35, 55, 75, 95, 115, 135, 155, 175, 195,
    16, 36, 56, 76, 96, 116, 136, 156, 176, 196,
    17, 37, 57, 77, 97, 117, 137, 157, 177, 197,
    18, 38, 58, 78, 98, 118, 138, 158, 178, 198,
    19, 39, 59, 79, 99, 119, 139, 159, 179, 199,
]
device = neopixel(width=10, height=20, rotate=0, mapping=HAT)
Tim = draw(device)
Thomas = playground.Playground(device.height, device.width)
for i in range(0,len(tetris_blocks.block_list)):
    Thomas.clear()
    Thomas.add_block(tetris_blocks.block_list[i])
    Tim.draw_playground(Thomas)
    time.sleep(2)
