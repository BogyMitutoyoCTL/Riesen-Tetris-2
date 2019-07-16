import time

import pygame
class Controller:


    def steuern(self):

        pygame.init()
        pygame.joystick.init()
        jc = pygame.joystick.get_count()
        print(jc)


        a = pygame.joystick.Joystick(0)
        a.init()
        while True:
            pygame.event.get()
            if a.get_button(1)>0.001:
                print("Rechts drehen!")


            if a.get_button(0)>0.001:
                print("links drehen!")


            if a.get_button(7)>0.001:
                print("Spiel beenden!")


            if a.get_axis(0)<-0.001:
                print("Gehe nach Links!")


            if a.get_axis(0)>0.001:
                print("Gehe nach Rechts!")


            if a.get_axis(1)>0.001:
                print("Gehe nach unten!")



            time.sleep(0.05)


pygame.quit()