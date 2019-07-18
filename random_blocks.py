import random
import tetris_blocks


class Randomblock:
    def __init__(self):
        number_of_possible_blocks = len(tetris_blocks.block_list)
        self.maximum = number_of_possible_blocks - 1

    def get_random_block(self):
        re = random.randint(0, self.maximum)
        return tetris_blocks.block_list[re]
