class GameSpeed:
    @staticmethod
    def game_speed(score):
        frame_rate = 20
        if score >= 50:
            frame_rate = 21
        if score >= 100:
            frame_rate = 22
        if score >= 200:
            frame_rate = 23
        if score >= 300:
            frame_rate = 24
        if score >= 400:
            frame_rate = 25
        if score >= 500:
            frame_rate = 26
        if score >= 1000:
            frame_rate = 27
        if score >= 3000:
            frame_rate = 28 * (0 + score/3000.0)
            if frame_rate > 60:
                frame_rate = 60
        return frame_rate


if __name__ == "__main__":
    for score in range(10000):
        st = GameSpeed.game_speed(score)
        print("Score: " + str(score) + " Sleeptime: " + str(st))