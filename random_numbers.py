import random


class Randomblock:
    def __init__(self):
        self.obergrenze = 7

    def get_random_block_number(self):
        ret = random.randint(1, self.obergrenze)
        return ret


rb = Randomblock()
print(rb.get_random_block_number())
