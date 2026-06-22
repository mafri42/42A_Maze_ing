class MazeGenerator:
    def __init__(self, width: int, height: int, entry: list, exit: list, perfect: bool, output: str) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Error: Width and Height have to be >0.")
        
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.output = output
        self.matrix: list[list[int]] = [[15 for _ in range(width)] for _ in range(height)]

    def print_matrix(self) -> None:
        for row in self.matrix:
            top = ""
            col = ""
            bot = ""
            for cell in row:
                if cell & 1:
                    top = top + "────"
                else:
                    top = top + "    "
                if cell & 8:
                    col = col + "│   "
                else:
                    col = col + "    "
            if row[-1] & 2:
                col = col + "│"
            print(top)
            print(col)
        for cell in self.matrix[-1]:
            if cell & 4:
                bot = bot + "────"
            else:
                bot = bot + "    "
        print(bot)

    def check(self) -> None:
        x, y = self.entry
        if (x < 0 or x > (self.width - 1)) or (y < 0 or y > (self.height - 1)):
            raise ValueError("entry coords wrong")




if __name__ == "__main__":
    maze = MazeGenerator(width=5, height=5, entry=[0,0], exit=[4,4], perfect=True, output="maze.txt")
    maze.print_matrix()
    maze.check()