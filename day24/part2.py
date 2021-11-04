import itertools
from typing import Tuple

from day24 import part1
from day24.common import moves, read_instructions


def solve(filename: str) -> int:
    instructions = read_instructions(filename)

    black_tiles = part1.lay_tiles(instructions)

    neighbourhood = tuple(move(0, 0) for move in moves.values())

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
    return len(black_tiles)


# noinspection PyTypeChecker
def add(*args) -> Tuple[int]:
    return tuple(sum(x) for x in zip(*args))
