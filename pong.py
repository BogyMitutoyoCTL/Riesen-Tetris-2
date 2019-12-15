import objects
import rgbleddrawer
import playground

def run_game():
    rgb_led_drawer = rgbleddrawer.RgbLedDrawer
    color_playground = playground.Playground(20, 10)
    i = 0
    while i<20:
        i+=1
    color_playground.clear()
    color_playground.add_object(objects.Objecttype.paddle_left)
    rgb_led_drawer.draw_playground(color_playground)

if __name__ == "__main__":
    while True:
        run_game()