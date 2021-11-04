from typing import List, Set, Tuple

from day24.common import moves, read_instructions


def solve(filename: str) -> int:
    instructions = read_instructions(filename)

    black_tiles = lay_tiles(instructions)

    return len(black_tiles)


def lay_tiles(instructions: List[List[str]]) -> Set[Tuple[int, int]]:
    black_tiles = set()
    for line in instructions:
        tile = (0, 0)
        for instruction in line:
            tile = moves[instruction](*tile)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    return black_tiles
