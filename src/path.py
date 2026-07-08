from collections import deque
from src.maze_generator import MazeGenerator


def bfs_alg(maze: MazeGenerator) -> str:
    d = deque([(maze.entry[0], maze.entry[1], "")])
    checked = set()
    checked.add((maze.entry[0], maze.entry[1]))
    while d:
        x, y, path = d.popleft()
        if (x, y) == maze.exit:
            return path
        point = maze.matrix[y][x]
        if (point & 1) == 0:
            nx, ny = x, y - 1
            if ny >= 0 and (nx, ny) not in checked:
                d.append((nx, ny, path + "N"))
                checked.add((nx, ny))
        if (point & 2) == 0:
            nx, ny = x + 1, y
            if nx < maze.width and (nx, ny) not in checked:
                d.append((nx, ny, path + "E"))
                checked.add((nx, ny))
        if (point & 4) == 0:
            nx, ny = x, y + 1
            if ny < maze.height and (nx, ny) not in checked:
                d.append((nx, ny, path + "S"))
                checked.add((nx, ny))
        if (point & 8) == 0:
            nx, ny = x - 1, y
            if nx >= 0 and (nx, ny) not in checked:
                d.append((nx, ny, path + "W"))
                checked.add((nx, ny))
    return path
