import sys
from parsing import config
from maze_generator import MazeGenerator


if __name__ == "__main__":
    data = config()
    maze = MazeGenerator(
        width=data['width'],
        height=data['height'],
        entry=data['entry'],
        exit=data['exit'],
        output=data['output_file'],
        perfect=data['perfect']
    )
    try:
        maze.check()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(f"\nLab {maze.width}x{maze.height} initialized!")
    maze.mazing()
    maze.print_matrix()
