import sys
from src.a_maze_ing import config, MazeRenderer, Pattern, bfs_alg, MazeOutput


if __name__ == "__main__":
    data = config()
    try:
        maze = Pattern(
            width=data['width'],
            height=data['height'],
            entry=data['entry'],
            exit=data['exit'],
            output=data['output_file'],
            perfect=data['perfect'],
            seed=data['seed']
        )
        maze.check()
        maze.mazing()
        path = bfs_alg(maze)
        maze.path_output(path)
        expo = MazeOutput(maze, path)
        expo.save()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(f"\nLab {maze.width}x{maze.height} initialized!")
    try:
        renderer = MazeRenderer(maze)
        renderer.interactive_menu()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
