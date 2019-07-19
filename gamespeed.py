import math


class GameSpeed:
    @staticmethod
    def game_speed(score, base_game_frame_rate=20):
        factor = math.exp(score / 1000.0)
        frame_rate = factor * base_game_frame_rate
        return frame_rate


if __name__ == "__main__":
    for score in range(10000):
        st = GameSpeed.game_speed(score)
        print("Score: " + str(score) + " Sleeptime: " + str(st))
