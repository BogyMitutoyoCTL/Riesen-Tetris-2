import Ball_Steuerung
import objects
def bot_steuerung(s:object,b:object):
    if s.posx-b.posx > 0 and s.posx > 0:
        s.posx -= 1
    if s.posx-b.posx < 0 and s.posx < 7:
        s.posx += 1