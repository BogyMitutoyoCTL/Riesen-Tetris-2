import time
import tetris_blocks
import pygame
import Colors

class Controller:


    def steuern(self):

        pygame.init()
        pygame.joystick.init()


        a = pygame.joystick.Joystick(0)
        a.init()
        pygame.event.get()
        if a.get_button(1)>0.001:
            print("Rechts drehen!")
            right = "Right!"
            return right


        if a.get_button(0)>0.001:
            print("links drehen!")
            e = tetris_blocks.Block(tetris_blocks.Blocktype.t, Colors.Block_color.yellow)
            e.rotation(-1)
            left = "Left!"
            return left


        if a.get_button(7)>0.001:
            print("Spiel beenden!")
            end = "End!"
            return end


        if a.get_axis(0)<-0.001:
            print("Gehe nach Links!")
            go_left = "Go Left!"
            return go_left


        if a.get_axis(0)>0.001:
            print("Gehe nach Rechts!")
            go_right = "Go Right!"
            return go_right


        if a.get_axis(1)>0.001:
            print("Gehe nach unten!")
            go_down =  "Go Down!"
            return  go_down


            time.sleep(0.05)


pygame.quit()