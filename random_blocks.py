import random
import tetris_blocks


class Randomblock:
    def __init__(self):
        lae = len(tetris_blocks.block_list)
        self.obergrenze = lae - 1

    def get_random_block(self):
        re = random.randint(0, self.obergrenze)
        return tetris_blocks.block_list[re]
