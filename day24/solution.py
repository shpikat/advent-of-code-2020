import itertools
import re
from typing import List, Set, Tuple


def part1(input_data: str) -> int:
    instructions = read_instructions(input_data)

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


def part2(input_data: str) -> int:
    instructions = read_instructions(input_data)

    black_tiles = lay_tiles(instructions)

    neighbourhood = tuple(move(0, 0) for move in moves.values())

    for day in range(100):
        black_tiles_not_flipped = (
            tile
            for tile in black_tiles
            if sum(1 for neighbour in neighbourhood if add(tile, neighbour) in black_tiles)
            in (1, 2)
        )
        white_tiles_flipped = (
            add(tile, candidate)
            for tile in black_tiles
            for candidate in neighbourhood
            if add(tile, candidate) not in black_tiles
            and sum(
                1 for neighbour in neighbourhood if add(tile, candidate, neighbour) in black_tiles
            )
            == 2
        )
        black_tiles = set(itertools.chain(black_tiles_not_flipped, white_tiles_flipped))
    return len(black_tiles)


# noinspection PyTypeChecker
def add(*args) -> Tuple[int]:
    return tuple(sum(x) for x in zip(*args))


pattern = re.compile("e|se|sw|w|ne|nw")

moves = {
    "e": lambda x, y: (x + 1, y),
    "se": lambda x, y: (x, y - 1),
    "sw": lambda x, y: (x - 1, y - 1),
    "w": lambda x, y: (x - 1, y),
    "nw": lambda x, y: (x, y + 1),
    "ne": lambda x, y: (x + 1, y + 1),
}


def read_instructions(input_data: str) -> List[List[str]]:
    return [pattern.findall(line) for line in input_data.splitlines() if line]
