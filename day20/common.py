import re
from dataclasses import dataclass
from typing import List

re_tile = re.compile(r'^Tile (\d+):$')


@dataclass(frozen=True)
class Tile:
    id: int
    image: List[str]


def read_tiles() -> List[Tile]:
    with open("input", "r") as file:
        return [read_tile(tile) for tile in (file.read().strip().split('\n\n'))]


def read_tile(tile: str) -> Tile:
    lines = tile.strip().split('\n')
    tile_id = int(re_tile.match(lines[0]).group(1))
    image = lines[1:]
    return Tile(tile_id, image)
