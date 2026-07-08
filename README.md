*This project has been created as part of the 42 curriculum by acastald, masacco.*

# A-Maze-ing

## Description
A-Maze-ing is a Python project developed for the 42 curriculum. It generates random mazes from a configuration file, guarantees reproducibility through a seed, computes the shortest path between the entry and exit using Breadth-First Search (BFS), saves the maze in the required hexadecimal format, and provides an interactive ASCII renderer.

## Features

- Random maze generation
- Perfect maze generation (Recursive Backtracker / DFS)
- Optional random seed for reproducibility
- Automatic shortest path computation (BFS)
- Interactive terminal visualization
- Show/Hide solution
- Change wall colors
- Export maze to the required hexadecimal format
- Embedded "42" pattern when the maze is large enough
- Reusable maze generator module

## Project Structure

```text
.
├── a_maze_ing.py
├── config.txt
├── maze.txt
├── Makefile
├── requirements.txt
└── src/
    └── a_maze_ing/
        ├── maze_generator.py
        ├── maze_render.py
        ├── path.py
        ├── output.py
        ├── parsing.py
        └── ft_pattern.py
```

## Installation

```bash
make install
```

or

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Running the project

```bash
make run
```

or

```bash
python3 a_maze_ing.py config.txt
```

## Configuration File

Example:

```ini
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=9,7
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=0
```

| Key | Description |
|------|-------------|
| WIDTH | Maze width |
| HEIGHT | Maze height |
| ENTRY | Entry coordinates |
| EXIT | Exit coordinates |
| OUTPUT_FILE | Output filename |
| PERFECT | Generate a perfect maze |
| SEED | Random seed (0 = random seed) |

## Output File

Each cell is stored as one hexadecimal digit representing the four walls.

Bits:

| Bit | Wall |
|----|------|
|0|North|
|1|East|
|2|South|
|3|West|

After an empty line the file contains:

1. Entry coordinates
2. Exit coordinates
3. Shortest path (N,E,S,W)

## Maze Generation Algorithm

This project uses the **Recursive Backtracker** algorithm (Depth-First Search).

Steps:

1. Start from the entry cell.
2. Visit random unvisited neighbours.
3. Remove the wall between cells.
4. Continue until no neighbours remain.
5. Backtrack using a stack.
6. Repeat until every reachable cell has been visited.

The shortest path is computed afterwards using **Breadth-First Search (BFS)**.

### Why this algorithm?

Recursive Backtracker was chosen because it:

- is simple to implement;
- generates perfect mazes;
- produces long natural corridors;
- is efficient in memory and execution time;
- perfectly fits the project requirements.

## Visual Representation

The maze is rendered directly in the terminal using ASCII characters.

Legend:

- Green: Entry
- Red: Exit
- Blue: Solution path
- Cyan: "42" pattern
- Colored walls

Interactive menu:

1. Generate a new maze
2. Show/Hide shortest path
3. Change wall colors
4. Quit

## Reusable Module

The reusable component is the `MazeGenerator` class.

Example:

```python
from a_maze_ing import MazeGenerator

maze = MazeGenerator(
    width=20,
    height=15,
    entry=(0,0),
    exit=(19,14),
    perfect=True,
    output="maze.txt",
    seed=42,
)

maze.check()
maze.mazing()
```

The generated maze is available through:

```python
maze.matrix
maze.path_coords
maze.path_string
```

## Makefile

| Command | Description |
|---------|-------------|
| make install | Install dependencies |
| make run | Execute project |
| make debug | Run with pdb |
| make lint | flake8 + mypy |
| make clean | Remove caches |
| make build | Build Python package |

## Error Handling

The project validates:

- invalid configuration files;
- invalid coordinates;
- missing files;
- malformed parameters;
- impossible maze dimensions;
- save errors.

Errors are handled gracefully using exceptions.

## Team & Project Management

### Roles

- Developer(s): implementation, testing and documentation.

### Planning

Initial goal:

- parser
- generator
- pathfinding
- renderer
- export

During development the project evolved by separating each responsibility into dedicated modules, making the code easier to maintain and reuse.

### What worked well

- Modular architecture
- Clear separation of responsibilities
- Reusable generator
- Interactive renderer

### Possible improvements

- Additional maze generation algorithms
- Graphical interface
- Animation during generation
- Unit tests
- Better color customization

### Tools

- Python 3
- flake8
- mypy
- Git
- Virtual Environment
- Make

## Resources

- https://docs.python.org/3/
- https://en.wikipedia.org/wiki/Maze_generation_algorithm
- https://en.wikipedia.org/wiki/Depth-first_search
- https://en.wikipedia.org/wiki/Breadth-first_search
- https://realpython.com/

### AI Usage

AI was used as a productivity tool to:

- improve documentation;
- review Markdown formatting;
- discuss implementation ideas;
- refine explanations.

All algorithms, implementation details and final validation were reviewed and understood by the project authors.

## License

This project was developed for educational purposes as part of the 42 curriculum.