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
        if self.entry == self.exit:
            raise ValueError("Entry and exit coord are the same")
        e_x, e_y = self.entry
        if (e_x < 0 or e_x > (self.width - 1)) or (e_y < 0 or e_y > (self.height - 1)):
            raise ValueError("entry coords wrong")
        u_x, u_y = self.exit
        if (u_x < 0 or u_x > (self.width - 1)) or (u_y < 0 or u_y > (self.height - 1)):
            raise ValueError("exit coords wrong")

    def move_first(self, current_x: int, current_y: int, visited: list[list[bool]]) -> list[tuple[int, int, str]]:
            valid_neighbors = []
            # nord y-1
            next_x = current_x
            next_y = current_y - 1
            if next_y >= 0 and not visited[next_y][next_x]:
                valid_neighbors.append((next_x, next_y, 'N'))
            # sud y+1
            next_x = current_x
            next_y = current_y + 1
            if next_y < self.height and not visited[next_y][next_x]:
                valid_neighbors.append((next_x, next_y, 'S'))
            # ovest x-1
            next_x = current_x - 1
            next_y = current_y
            if next_x >= 0 and not visited[next_y][next_x]:
                valid_neighbors.append((next_x, next_y, 'W'))
            # 4. est x+1
            next_x = current_x + 1
            next_y = current_y
            if next_x < self.width and not visited[next_y][next_x]:
                valid_neighbors.append((next_x, next_y, 'E'))
            
            return valid_neighbors
    
    def wreck_it_ralph(self, current_x: int, current_y: int, next_x: int, next_y: int, dir: str) -> None:
        if dir == 'N':
            self.matrix[current_y][current_x] -= 1
            self.matrix[next_y][next_x] -= 4
        elif dir == 'S':
            self.matrix[current_y][current_x] -= 4
            self.matrix[next_y][next_x] -= 1
        elif dir == 'W':
            self.matrix[current_y][current_x] -= 8
            self.matrix[next_y][next_x] -= 2
        elif dir == 'E':
            self.matrix[current_y][current_x] -= 2
            self.matrix[next_y][next_x] -= 8

if __name__ == "__main__":
    maze = MazeGenerator(width=5, height=5, entry=[0,0], exit=[4,4], perfect=True, output="maze.txt")
    maze.print_matrix()
    maze.check()