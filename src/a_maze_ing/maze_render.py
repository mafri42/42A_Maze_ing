from .ft_pattern import Pattern
import os


class MazeRenderer:
    def __init__(self, maze_gen, ft_coords) -> None:
        self.maze = maze_gen
        self.show_path = False

        self.WALL_COLORS = [
            "\033[37m",  # 0: Bianco
            "\033[36m",  # 1: Ciano
            "\033[32m",  # 2: Verde
            "\033[35m",  # 3: Magenta
            "\033[33m",  # 4: Giallo
            "\033[31m",  # 5: Rosso
        ]
        self.current_color_idx = 0  # Indice del colore attuale

        self.RESET = "\033[0m"
        self.ENTRY_COLOR = "\033[45m"  # Sfondo Magenta per l'ingresso
        self.EXIT_COLOR = "\033[41m"   # Sfondo Rosso per l'uscita
        self.PATH_COLOR = "\033[44m"   # Sfondo Blu per il cammino
        self.FORTY_TWO_COLOR = "\033[42m"  # Sfondo Verde per le celle del 42

        self.ft_coords = ft_coords
        self.path_coords = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        matrix = self.maze.matrix
        wall_color = self.WALL_COLORS[self.current_color_idx]
        for y, row in enumerate(matrix):
            top = ""
            col = ""
            for x, cell in enumerate(row):
                if cell & 1:
                    top += f"{wall_color}+───{self.RESET}"
                else:
                    top += f"{wall_color}+{self.RESET}   "
                if cell & 8:
                    col += f"{wall_color}│{self.RESET}"
                else:
                    col += " "
                if (x, y) == self.maze.entry:
                    col += f"{self.ENTRY_COLOR}   {self.RESET}"
                elif (x, y) == self.maze.exit:
                    col += f"{self.EXIT_COLOR}   {self.RESET}"
                elif self.show_path and (x, y) in self.path_coords:
                    col += f"{self.PATH_COLOR}   {self.RESET}"
                elif (x, y) in self.ft_coords:
                    col += f"{self.FORTY_TWO_COLOR}   {self.RESET}"
                else:
                    col += "   "
            top += f"{wall_color}+{self.RESET}"
            if row[-1] & 2:  # Est (Bit 1) dell'ultima cella
                col += f"{wall_color}│{self.RESET}"
            else:
                col += " "
            print(top)
            print(col)
        bot = ""
        for cell in matrix[-1]:
            if cell & 4:
                bot += f"{wall_color}+───{self.RESET}"
            else:
                bot += f"{wall_color}+{self.RESET}   "
        bot += f"{wall_color}+{self.RESET}"
        print(bot)

    def interactive_menu(self):
        while True:
            self.clear_screen()
            self.draw()
            print("\n=== A-Maze-ing ===")
            print("1. Re-generate a new maze")
            print("2. Show/Hide path from entry to exit")
            print("3. Change maze wall colors")
            print("4. Quit")
            choice = input("Choice? (1-4): ")
            if choice == '1': 
                self.maze.matrix = [[15 for _ in range(self.maze.width)] for _ in range(self.maze.height)]
                self.maze.mazing()
            elif choice == '2':
                self.show_path = not self.show_path
            elif choice == '3':
                self.current_color_idx = (self.current_color_idx + 1) % len(self.WALL_COLORS)
            elif choice == '4':
                break
