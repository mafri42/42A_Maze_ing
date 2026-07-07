class MazeOutput:
    def __init__(self, maze_gen, path_string: str) -> None:
        self.maze = maze_gen
        self.path_string = path_string

    def save(self) -> None:
        """Formatta e salva i dati del labirinto nel file di output."""
        try:
            with open(self.maze.output, "w") as file:
                # 1. Matrice in formato Esadecimale (X maiuscolo)
                for row in self.maze.matrix:
                    hex_row = "".join(f"{cell:X}" for cell in row)
                    file.write(hex_row + "\n")
                
                # 2. Riga vuota
                file.write("\n")
                
                # 3. Coordinate ingresso
                file.write(f"{self.maze.entry[0]},{self.maze.entry[1]}\n")
                
                # 4. Coordinate uscita
                file.write(f"{self.maze.exit[0]},{self.maze.exit[1]}\n")
                
                # 5. Percorso Risolutivo
                file.write(f"{self.path_string}\n")
                
            print(f"[*] File di output generato: '{self.maze.output}'")
            
        except IOError as e:
            raise ValueError(f"Impossibile salvare il file: {e}")