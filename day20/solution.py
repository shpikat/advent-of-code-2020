from __future__ import annotations

import operator
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import reduce
from itertools import product
from math import sqrt
from typing import Callable, Dict, List, Set, Tuple

transformations = [
    lambda tile: tile,
    lambda tile: rotate_90(tile),
    lambda tile: rotate_180(tile),
    lambda tile: rotate_90(rotate_180(tile)),
    lambda tile: flip_horizontally(tile),
    lambda tile: rotate_90(flip_vertically(tile)),
    lambda tile: flip_vertically(tile),
    lambda tile: rotate_90(flip_horizontally(tile)),
]


@dataclass(frozen=True)
class TileAndEdges:
    tile: Tile
    edges: List[str]


def part1(input_data: str) -> int:
    tiles = read_tiles(input_data)

    # We can easily find the corner tiles, get the answer and pass, but the task explicitly says:
    # "Your first task is to reassemble the original image by orienting the tiles so they fit together."
    # So-o-o, "Image! Assemble!"

    arranged_tiles = assemble_image(tiles)

    # Print the image
    # tile_size = len(arranged_tiles[0][0].image)
    # for row in arranged_tiles:
    #     for line_number in range(tile_size):
    #         print('  '.join(tile.image[line_number] for tile in row))
    #     print()

    return reduce(operator.mul, (arranged_tiles[i][j].id for i, j in product((0, -1), repeat=2)))


def assemble_image(tiles: List[Tile]) -> List[List[Tile]]:
    matching_edges = get_matching_edges(tiles)

    image_size = int(sqrt(len(tiles)))

    # Didn't find a way to use comprehensions and let the code remain readable

    row = [find_starting_tile(matching_edges)]
    for position_in_row in range(1, image_size):
        tile_to_the_left = row[position_in_row - 1]
        row.append(
            rotate_90(find_and_match(matching_edges, tile_to_the_left, get_matching_for_right_edge))
        )
    arranged_tiles = [row]

    for row_number in range(1, image_size):
        row = []
        for position_in_row in range(image_size):
            tile_to_the_top = arranged_tiles[row_number - 1][position_in_row]
            row.append(
                find_and_match(matching_edges, tile_to_the_top, get_matching_for_bottom_edge)
            )
        arranged_tiles.append(row)
    return arranged_tiles


def get_matching_edges(tiles: List[Tile]) -> Dict[str, List[TileAndEdges]]:
    matching_edges = defaultdict(list)
    for tile in tiles:
        edges = get_edges(tile.image)
        t = TileAndEdges(tile, edges)
        for edge in edges:
            matching_edges[edge].append(t)
    return matching_edges


def get_edges(image: List[str]) -> List[str]:
    top = image[0]
    right = column_to_row(image, -1)
    bottom_reversed = image[-1]
    left_reversed = column_to_row(image, 0)
    return [
        top,
        right,
        bottom_reversed[::-1],
        left_reversed[::-1],
        top[::-1],
        right[::-1],
        bottom_reversed,
        left_reversed,
    ]


def find_starting_tile(matching_edges: Dict[str, List[TileAndEdges]]) -> Tile:
    border_tiles = Counter()
    for tiles in matching_edges.values():
        if len(tiles) == 1:
            tile, edges = tiles[0].tile, tiles[0].edges
            border_tiles[tile.id] += 1

            # We are looking for two pairs (original and reversed) of non-matched edges
            if border_tiles[tile.id] == 4:
                corner_edges = [i for i, e in enumerate(edges[:4]) if len(matching_edges[e]) == 1]
                is_1_next_to_0 = corner_edges[0] + 1 == corner_edges[1]
                top_edge = corner_edges[1] if is_1_next_to_0 else corner_edges[0]
                return transformations[top_edge](tile)
    print("Ambiguous input: no definite corner tiles")


def find_and_match(matching_edges, neighbour_tile: Tile, get_edge: Callable[[Tile], str]) -> Tile:
    edge = get_edge(neighbour_tile)
    tile, edges = next(
        (tile_edges.tile, tile_edges.edges)
        for tile_edges in matching_edges[edge]
        if tile_edges.tile.id != neighbour_tile.id
    )
    transformed = transformations[edges.index(edge)](tile)
    return transformed


def get_matching_for_bottom_edge(tile: Tile) -> str:
    return tile.image[-1]


def get_matching_for_right_edge(tile: Tile) -> str:
    return column_to_row(tile.image, -1)[::-1]


def column_to_row(image: List[str], index: int) -> str:
    return "".join(line[index] for line in image)


def rotate_90(tile: Tile) -> Tile:
    return Tile(
        tile.id,
        [
            "".join(line[column] for line in tile.image)
            for column in reversed(range(len(tile.image[0])))
        ],
    )


def rotate_180(tile: Tile) -> Tile:
    return Tile(tile.id, [line[::-1] for line in reversed(tile.image)])


def flip_vertically(tile: Tile) -> Tile:
    return Tile(tile.id, tile.image[::-1])


def flip_horizontally(tile: Tile) -> Tile:
    return Tile(tile.id, [line[::-1] for line in tile.image])


re_tile = re.compile(r"^Tile (\d+):$")


@dataclass(frozen=True)
class Tile:
    id: int
    image: List[str]


@dataclass(frozen=True)
class Matrix:
    data: Set[Tuple[int, int]]
    width: int
    height: int

    @classmethod
    def digitize(cls, image: List[str]) -> Matrix:
        return Matrix(
            {(x, y) for y, line in enumerate(image) for x, ch in enumerate(line) if ch == "#"},
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
        return "\n".join(
            "".join("#" if (x, y) in self.data else "." for x in range(self.width))
            for y in range(self.height)
        )


def part2(input_data: str) -> int:
    tiles = read_tiles(input_data)

    image = strip_borders(assemble_image(tiles))
    sea = Matrix.digitize(image)

    raw_monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #      
"""
    monster = Matrix.digitize(raw_monster.strip("\n").splitlines())

    return get_roughness(sea, monster)


def strip_borders(tiles: List[List[Tile]]) -> List[str]:
    tile_size_no_borders = len(tiles[0][0].image) - 1
    return [
        "".join(tile.image[line_number][1:-1] for tile in row)
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


def read_tiles(input_data: str) -> List[Tile]:
    return [read_tile(tile) for tile in (input_data.split("\n\n"))]


def read_tile(tile: str) -> Tile:
    lines = tile.strip().splitlines()
    tile_id = int(re_tile.match(lines[0]).group(1))
    image = lines[1:]
    return Tile(tile_id, image)
