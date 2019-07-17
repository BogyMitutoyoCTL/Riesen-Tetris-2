import time


class Points:
    re_weg = 10
    new_block = 1

    def points(self, all_points, reihe_weg, new):

        if reihe_weg == 1:
            all_points += 10

        if reihe_weg == 2:
            all_points += 30

        if reihe_weg == 3:
            all_points += 50

        if reihe_weg == 4:
            all_points += 100

        if new == 1:
            all_points += 1

        return all_points


end_points = 0
a = Points()

end_points += a.points(0, 1, 1)
end_points += a.points(0, 2, 1)

print(end_points)

time.sleep(10)
