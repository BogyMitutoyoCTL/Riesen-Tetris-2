import tetris_blocks
import numbersforscore


class NumberToBlock():
    def get_block(self, number: int):
        numbers_list = self.get_list_of_single_numbers(number)

        for number in numbers_list:
            number_block = self.get_digit_block(number)
            print("Number: " + str(number))
            print(number_block.draw_block())

        # draw_digit(i % 10, 10, 0, red_playground, red_drawer)
        # draw_digit(dritte_nummer % 10, 15, 0, red_playground, red_drawer)
        # draw_digit(zweite_nummer % 10, 20, 0, red_playground, red_drawer)
        # draw_digit(erste_nummer % 10, 25, 0, red_playground, red_drawer)

    @staticmethod
    def get_digit_block(i):
        digit = numbersforscore.NumbersForScore.number[i]
        rotatable = [digit] * 4
        b = tetris_blocks.Block(rotatable, tetris_blocks.Block_color.red)
        return b

    @staticmethod
    def get_list_of_single_numbers(number: int):
        numbers_list = [number % 10, number // 10 % 10, number // 100 % 10, number // 1000 % 10]
        return numbers_list


nb = NumberToBlock()
nb.get_block(98876)
