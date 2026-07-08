import random
from .maze_generator import MazeGenerator


class Pattern(MazeGenerator):
    def mazing(self) -> None:
        checked: list[list[bool]] = [[False for _ in range(self.width)]
                                     for _ in range(self.height)]
        self.forty_two_coords = []
        if self.width <= 9 or self.height <= 7:
            print("Error: The maze size does not allow the '42' pattern.")
        else:
            self.move_x = round((self.width - 7) / 2)
            self.move_y = round((self.height - 5) / 2)
            self.pattern_ft = [
                (0, 0), (4, 0), (5, 0), (6, 0), (0, 1), (6, 1), (0, 2), (1, 2),
                (2, 2), (4, 2), (5, 2), (6, 2), (2, 3), (4, 3), (2, 4), (4, 4),
                (5, 4), (6, 4)
            ]
            for ft_x, ft_y in self.pattern_ft:
                x = self.move_x + ft_x
                y = self.move_y + ft_y
                self.forty_two_coords.append((x, y))
                if (x, y) != self.entry and (x, y) != self.exit:
                    checked[y][x] = True
        e_x, e_y = self.entry
        checked[e_y][e_x] = True
        stacked: list[tuple[int, int]] = [(e_x, e_y)]
        while stacked:
            e_x, e_y = stacked[-1]
            valid = self.move_first(e_x, e_y, checked)
            if valid:
                next_x, next_y, dir = random.choice(valid)
                checked[next_y][next_x] = True
                self.wreck_it_ralph(e_x, e_y, next_x, next_y, dir)
                stacked.append((next_x, next_y))
            else:
                stacked.pop()
