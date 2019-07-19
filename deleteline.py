import playground


class FullLineDetector:
    def __init__(self):
        pass

    def detect_lines(self, playground: playground.Playground):
        full_lines = []
        for line in range(0, playground.height):
            line_is_full = True
            for x in range(0, playground.width):
                pixel = playground.get_pixel(x, line)
                if pixel[0] + pixel[1] + pixel[2] == 0:
                    line_is_full = False
                    break
            if line_is_full:
                full_lines.append(line)
        return full_lines

    def delete_full_lines(self, full_lines_list, playground: playground.Playground):
        for line in full_lines_list:
            for line_above in range(line, 1, -1):
                for x in range(playground.width):
                    color_from_above = playground.get_pixel(x, line_above-1)
                    playground.set_pixel(x, line_above, color_from_above)
            for x in range(playground.width):
                playground.set_pixel(x, 0, (0,0,0))
