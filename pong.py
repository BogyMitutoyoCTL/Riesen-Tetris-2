import objects
import rgbleddrawer
import playground

def run_game():
    rgb_led_drawer = rgbleddrawer.RgbLedDrawer
    color_playground = playground.Playground(20, 10)
    color_playground.clear()
    color_playground.add_object(objects.Objecttype.paddle_left,0,6)
    rgb_led_drawer.draw_playground(color_playground)
    time.sleep(20)
    color_playground.clear()

if __name__ == "__main__":
    while True:
        run_game()