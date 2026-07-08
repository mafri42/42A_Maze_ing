class MazeOutput:
    def __init__(self, maze_gen, path_string: str) -> None:
        self.maze = maze_gen
        self.path_string = path_string

    def save(self) -> None:
        try:
            with open(self.maze.output, "w") as file:
                for row in self.maze.matrix:
                    hex_row = "".join(f"{cell:X}" for cell in row)
                    file.write(hex_row + "\n")
                file.write(f"\n{self.maze.entry[0]},{self.maze.entry[1]}\n")
                file.write(f"{self.maze.exit[0]},{self.maze.exit[1]}\n")
                file.write(f"{self.path_string}\n")
        except IOError as e:
            raise ValueError(f"Couldn't save the file: {e}")
