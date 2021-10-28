from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set, Tuple

from day20.common import read_tiles, Tile
from day20.part1 import assemble_image


@dataclass(frozen=True)
class Matrix:
    data: Set[Tuple[int, int]]
    width: int
    height: int

    @classmethod
    def digitize(cls, image: List[str]) -> Matrix:
        return Matrix(
            {(x, y) for y, line in enumerate(image) for x, ch in enumerate(line) if ch == '#'},
            len(image[0]),
            len(image),
        )

    def copy(self) -> Matrix:
        return Matrix(self.data.copy(), self.width, self.height)

    def flipped(self) -> Matrix:
        return Matrix({(self.width - 1 - x, y) for x, y in self.data}, self.width, self.height)

    def rotated(self) -> Matrix:
        return Matrix({(y, self.width - 1 - x) for x, y in self.data}, self.height, self.width)

    def calculate_difference_number(self, pattern: Matrix) -> int:
        working_copy = self.data.copy()

        for offset_y in range(self.height - pattern.height):
            for offset_x in range(self.width - pattern.width):
                next_match = {(offset_x + x, offset_y + y) for x, y in pattern.data}
                if next_match.issubset(working_copy):
                    working_copy.difference_update(next_match)
        return len(working_copy)

    def __repr__(self):
        return '\n'.join(
            ''.join('#' if (x, y) in self.data else '.' for x in range(self.width))
            for y in range(self.height)
        )


def main():
    tiles = read_tiles()

    image = strip_borders(assemble_image(tiles))
    sea = Matrix.digitize(image)

    raw_monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #      
'''
    monster = Matrix.digitize(raw_monster.strip('\n').split('\n'))

    print(get_roughness(sea, monster))


def strip_borders(tiles: List[List[Tile]]) -> List[str]:
    tile_size_no_borders = len(tiles[0][0].image) - 1
    return [
        ''.join(tile.image[line_number][1:-1] for tile in row)
        for row in tiles
        for line_number in range(1, tile_size_no_borders)
    ]


def get_roughness(sea: Matrix, monster: Matrix) -> int:
    nothing_detected = len(sea.data)
    for flip in (equal, flipped):
        matrix = flip(sea)
        for i in range(4):
            matrix = matrix.rotated()
            roughness = matrix.calculate_difference_number(monster)
            if roughness != nothing_detected:
                return roughness


def equal(matrix: Matrix) -> Matrix:
    return matrix.copy()


def flipped(matrix: Matrix) -> Matrix:
    return matrix.flipped()


if __name__ == "__main__":
    main()
