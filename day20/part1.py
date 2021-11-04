import operator
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import reduce
from itertools import product
from math import sqrt
from typing import Callable, Dict, List

from day20.common import Tile, read_tiles

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


def solve(filename: str) -> int:
    tiles = read_tiles(filename)

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
        row.append(rotate_90(find_and_match(matching_edges, tile_to_the_left, get_matching_for_right_edge)))
    arranged_tiles = [row]

    for row_number in range(1, image_size):
        row = []
        for position_in_row in range(image_size):
            tile_to_the_top = arranged_tiles[row_number - 1][position_in_row]
            row.append(find_and_match(matching_edges, tile_to_the_top, get_matching_for_bottom_edge))
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
                top_edge = corner_edges[1] if corner_edges[0] + 1 == corner_edges[1] else corner_edges[0]
                return transformations[top_edge](tile)
    print("Ambiguous input: no definite corner tiles")


def find_and_match(matching_edges, neighbour_tile: Tile, get_edge: Callable[[Tile], str]) -> Tile:
    edge = get_edge(neighbour_tile)
    tile, edges = next((tile_edges.tile, tile_edges.edges)
                       for tile_edges in matching_edges[edge]
                       if tile_edges.tile.id != neighbour_tile.id)
    transformed = transformations[edges.index(edge)](tile)
    return transformed


def get_matching_for_bottom_edge(tile: Tile) -> str:
    return tile.image[-1]


def get_matching_for_right_edge(tile: Tile) -> str:
    return column_to_row(tile.image, -1)[::-1]


def column_to_row(image: List[str], index: int) -> str:
    return ''.join(line[index] for line in image)


def rotate_90(tile: Tile) -> Tile:
    return Tile(tile.id, [
        ''.join(line[column] for line in tile.image)
        for column in reversed(range(len(tile.image[0])))
    ])


def rotate_180(tile: Tile) -> Tile:
    return Tile(tile.id, [line[::-1] for line in reversed(tile.image)])


def flip_vertically(tile: Tile) -> Tile:
    return Tile(tile.id, tile.image[::-1])


def flip_horizontally(tile: Tile) -> Tile:
    return Tile(tile.id, [line[::-1] for line in tile.image])
