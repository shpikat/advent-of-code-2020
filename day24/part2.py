import itertools
from typing import Tuple

from day24.common import read_instructions

moves = {
    'e': lambda x, y: (x + 1, y),
    'se': lambda x, y: (x, y - 1),
    'sw': lambda x, y: (x - 1, y - 1),
    'w': lambda x, y: (x - 1, y),
    'nw': lambda x, y: (x, y + 1),
    'ne': lambda x, y: (x + 1, y + 1),
}


def main():
    instructions = read_instructions()

    neighbourhood = tuple(move(0, 0) for move in moves.values())

    black_tiles = set()
    for line in instructions:
        tile = (0, 0)
        for instruction in line:
            tile = moves[instruction](*tile)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    for day in range(100):
        black_tiles_not_flipped = (
            tile
            for tile in black_tiles
            if sum(1 for neighbour in neighbourhood
                   if add(tile, neighbour) in black_tiles) in (1, 2)
        )
        white_tiles_flipped = (
            add(tile, candidate)
            for tile in black_tiles
            for candidate in neighbourhood
            if add(tile, candidate) not in black_tiles and sum(1 for neighbour in neighbourhood
                                                               if add(tile, candidate, neighbour) in black_tiles) == 2
        )
        black_tiles = set(itertools.chain(black_tiles_not_flipped, white_tiles_flipped))
    print(len(black_tiles))


# noinspection PyTypeChecker
def add(*args) -> Tuple[int]:
    return tuple(sum(x) for x in zip(*args))


if __name__ == "__main__":
    main()
