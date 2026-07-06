import sys
from src.a_maze_ing.parsing import config
from src.a_maze_ing.maze_generator import MazeGenerator
from src.a_maze_ing.maze_render import MazeRenderer
from src.a_maze_ing.ft_pattern import Pattern


if __name__ == "__main__":
    data = config()
    maze = Pattern(
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
        maze.mazing()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(f"\nLab {maze.width}x{maze.height} initialized!")
    try:
        renderer = MazeRenderer(maze, maze.pattern_ft)
        renderer.interactive_menu()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
