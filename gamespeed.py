class GameSpeed:
    @staticmethod
    def game_speed(score):
        sleep_time = 0
        if score >= 50:
            sleep_time = 0.35
        if score >= 100:
            sleep_time = 0.3
        if score >= 200:
            sleep_time = 0.28
        if score >= 300:
            sleep_time = 0.26
        if score >= 400:
            sleep_time = 0.24
        if score >= 500:
            sleep_time = 0.20
        if score >= 1000:
            sleep_time = 0.15
        if score >= 5000:
            sleep_time = 5
        return sleep_time
