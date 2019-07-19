import tetris_blocks
import numbersforscore
import color


class NumberToBlock:
    @staticmethod
    def get_block(number: int):
        numbers_list = NumberToBlock.get_list_of_single_numbers(number)

        blocks = []
        for number in numbers_list:
            block = numbersforscore.NumbersForScore.number[number]
            blocks.append(block)

        # Create Empty Array...
        field = NumberToBlock.create_number_field(blocks)

        single_block_width = len(blocks[len(blocks) - 1])
        for block_index in range(len(blocks) - 1, -1, -1):
            for line_index in range(len(blocks[block_index])):
                for pos_index in range(len(blocks[block_index])):
                    pos = blocks[block_index][line_index][pos_index]
                    field_x = line_index
                    field_y = block_index * single_block_width + pos_index
                    field[field_x][field_y] = pos

        return tetris_blocks.Block([field] * 4, color.BlockColor.red)

    @staticmethod
    def create_number_field(blocks):
        single_block_width = len(blocks[len(blocks) - 1])
        field = []
        for line in range(single_block_width):
            line = []
            for line_pos in range(0, len(blocks) * single_block_width):
                line.append(0)
            field.append(line)
        return field

    @staticmethod
    def get_list_of_single_numbers(number: int):
        numbers_list = [number // 1000 % 10, number // 100 % 10,number // 10 % 10, number % 10]
        return numbers_list
