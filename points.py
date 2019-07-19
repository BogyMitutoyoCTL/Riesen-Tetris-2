class Points:
    def points(self, all_points, number_of_deleted_lines, new):

        if number_of_deleted_lines == 1:
            all_points += 10


        if number_of_deleted_lines == 2:
            all_points += 30

        if number_of_deleted_lines == 3:
            all_points += 50

        if number_of_deleted_lines == 4:
            all_points += 100

        if new == 1:
            all_points += 1

        return all_points
