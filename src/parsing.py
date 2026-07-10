import sys
import os
from typing import TypedDict


class ConfigData(TypedDict):
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int


def config() -> ConfigData:
    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)
    elif len(sys.argv) != 2:
        print("Too few arguments")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        try:
            # if filename != "config.txt":
            #     raise ValueError(f"it's not the right file '{filename}'")
            if os.path.basename(sys.argv[0]) != "a_maze_ing.py":
                raise ValueError(f"it's not the right file '{sys.argv[0]}'")
            with open(sys.argv[1], "r") as file:
                data_dict = {}
                for i in file:
                    line = i.strip()
                    if line.startswith("#") or not line:
                        continue
                    if '=' not in i:
                        raise ValueError(f"Missing '=' in: {i}")
                    key, value = line.split("=", 1)
                    data_dict[key.strip().upper()] = value.strip()
                width = int(data_dict['WIDTH'])
                height = int(data_dict['HEIGHT'])
                entry_coord = [int(x) for x in data_dict['ENTRY'].split(',')]
                if len(entry_coord) != 2:
                    raise ValueError("Invalid parameter")
                exit_coord = [int(x) for x in data_dict['EXIT'].split(',')]
                if len(exit_coord) != 2:
                    raise ValueError("Invalid parameter")
                output_file = data_dict['OUTPUT_FILE']
                seed = int(data_dict['SEED'])
                if not seed:
                    seed = 0
                else:
                    seed = int(seed)
                not_perfect = data_dict['PERFECT'].lower()
                if not_perfect == 'true':
                    perfect = True
                elif not_perfect == 'false':
                    perfect = False
                else:
                    raise ValueError("PERFECT should be 'true' or"
                                     f"'false', not '{not_perfect}'")
                return {
                    'width': width,
                    'height': height,
                    'entry': (entry_coord[0], entry_coord[1]),
                    'exit': (exit_coord[0], exit_coord[1]),
                    'output_file': output_file,
                    'perfect': perfect,
                    'seed': seed
                }
        except FileNotFoundError as e:
            print(f"[STDERR] Error opening '{filename}': {e}")
            sys.exit(1)
        except ValueError as e:
            print(f"Error opening file '{filename}': {e}")
            sys.exit(1)
        except KeyError as e:
            print(f"Missing key in {filename}: {e}")
            sys.exit(1)
