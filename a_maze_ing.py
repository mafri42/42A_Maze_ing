import sys
from a_maze_ing.parsing import config
from a_maze_ing.maze_generator import MazeGenerator


if __name__ == "__main__":
    data = config()
    maze = MazeGenerator(
        width=data['width'],
        height=data['height'],
        entry=data['entry'],
        exit=data['exit'],
        output=data['output_file'],
        perfect=data['perfect'],
        seed=data['seed']
    )
    try:
        maze.check()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(f"\nLab {maze.width}x{maze.height} initialized!")
    maze.mazing()
    maze.print_matrix()
