import controller
import tetris_blocks


class Rotater():
    def control(self, controller: controller.Controller, blo: tetris_blocks.Block, position):

        controller.get_button_pressed(blo, position)
        return position
